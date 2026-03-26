from __future__ import annotations

import importlib
import pkgutil
from dataclasses import dataclass
from types import ModuleType
from typing import Any

_MIN_INSTRUCTION_VARIANTS = 5
_GENERIC_INSTRUCTION_FALLBACKS = (
    "Solve {problem}.",
    "Compute {problem}.",
    "Evaluate {problem}.",
    "Find the result for {problem}.",
    "Work through {problem}.",
)


@dataclass
class ModuleInfoView:
    module_id: str
    name: str
    topic: str
    subtopic: str = ""
    difficulty_levels: list[str] | None = None
    enabled: bool = True
    raw: Any = None


def _coerce_info(raw: Any, fallback_module_id: str) -> ModuleInfoView:
    if isinstance(raw, dict):
        module_id = raw.get("module_id") or fallback_module_id
        name = raw.get("name") or module_id.rsplit(".", 1)[-1].replace("_", " ").title()
        topic = raw.get("topic") or module_id.split(".", 1)[0]
        subtopic = raw.get("subtopic") or module_id.rsplit(".", 1)[-1]
        difficulty_levels = raw.get("difficulty_levels") or raw.get("levels") or []
        enabled = raw.get("enabled", True)
        return ModuleInfoView(module_id, name, topic, subtopic, list(difficulty_levels), enabled, raw)

    module_id = getattr(raw, "module_id", None) or fallback_module_id
    name = getattr(raw, "name", None) or module_id.rsplit(".", 1)[-1].replace("_", " ").title()
    topic = getattr(raw, "topic", None) or module_id.split(".", 1)[0]
    subtopic = getattr(raw, "subtopic", None) or module_id.rsplit(".", 1)[-1]
    difficulty_levels = getattr(raw, "difficulty_levels", None) or getattr(raw, "levels", None) or []
    enabled = getattr(raw, "enabled", True)
    return ModuleInfoView(module_id, name, topic, subtopic, list(difficulty_levels), enabled, raw)


def _ensure_instruction_variance(module: ModuleType) -> None:
    for attr_name in ("INSTRUCTION_TEMPLATES", "INSTRUCTIONS"):
        templates = getattr(module, attr_name, None)
        if templates is None:
            continue

        try:
            variants = [str(item) for item in templates if str(item).strip()]
        except TypeError:
            continue

        if len(variants) >= _MIN_INSTRUCTION_VARIANTS:
            continue

        for fallback in _GENERIC_INSTRUCTION_FALLBACKS:
            if fallback not in variants:
                variants.append(fallback)
            if len(variants) >= _MIN_INSTRUCTION_VARIANTS:
                break

        if isinstance(templates, list):
            templates[:] = variants
        elif isinstance(templates, tuple):
            setattr(module, attr_name, tuple(variants))
        else:
            setattr(module, attr_name, variants)


class ModuleRegistry:
    def __init__(self, package_name: str = "atlas_math.modules") -> None:
        self.package_name = package_name
        self._modules: dict[str, ModuleType] = {}
        self._info: dict[str, ModuleInfoView] = {}
        self._errors: dict[str, str] = {}
        self.refresh()

    def refresh(self) -> None:
        self._modules.clear()
        self._info.clear()
        self._errors.clear()

        package = importlib.import_module(self.package_name)
        for item in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
            if item.ispkg:
                continue
            try:
                module = importlib.import_module(item.name)
                if not hasattr(module, "MODULE_INFO") or not hasattr(module, "generate"):
                    continue
                _ensure_instruction_variance(module)
                fallback_module_id = item.name.replace(f"{self.package_name}.", "")
                info = _coerce_info(getattr(module, "MODULE_INFO"), fallback_module_id)
                if info.enabled:
                    self._modules[info.module_id] = module
                    self._info[info.module_id] = info
            except Exception as exc:  # pragma: no cover
                self._errors[item.name] = f"{type(exc).__name__}: {exc}"

    def modules(self) -> dict[str, ModuleType]:
        return dict(self._modules)

    def topics(self) -> list[str]:
        return sorted({info.topic for info in self._info.values()})

    def modules_by_topic(self, topic: str) -> dict[str, ModuleType]:
        return {mid: mod for mid, mod in self._modules.items() if self._info[mid].topic == topic}

    def errors(self) -> dict[str, str]:
        return dict(self._errors)

    def get(self, module_id: str) -> ModuleType | None:
        return self._modules.get(module_id)

    def info(self, module_id: str) -> ModuleInfoView | None:
        return self._info.get(module_id)


_GLOBAL_REGISTRY: ModuleRegistry | None = None


def get_registry() -> ModuleRegistry:
    global _GLOBAL_REGISTRY
    if _GLOBAL_REGISTRY is None:
        _GLOBAL_REGISTRY = ModuleRegistry()
    return _GLOBAL_REGISTRY
