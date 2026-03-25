from __future__ import annotations

import json
import random
from collections import Counter
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

from atlas_math.schemas import Sample


def _sample_to_dict(sample: Any, export_format: str = "clean") -> dict[str, Any]:
    if sample is None:
        raise TypeError("Sample is None")

    if hasattr(sample, "to_dict"):
        return sample.to_dict(export_format=export_format)

    if is_dataclass(sample):
        data = asdict(sample)
    elif isinstance(sample, dict):
        data = dict(sample)
    elif hasattr(sample, "__dict__"):
        data = dict(sample.__dict__)
    else:
        raise TypeError(f"Unsupported sample type: {type(sample).__name__}")

    if export_format == "clean":
        return {
            "instruction": data.get("instruction", ""),
            "input": data.get("input", ""),
            "answer": str(data.get("answer", "")),
            "answer_words": data.get("answer_words", ""),
        }
    if export_format == "extended":
        return {
            "instruction": data.get("instruction", ""),
            "input": data.get("input", ""),
            "answer": str(data.get("answer", "")),
            "answer_words": data.get("answer_words", ""),
            "difficulty": data.get("difficulty", ""),
            "topic": data.get("topic", ""),
            "subtopic": data.get("subtopic", ""),
        }
    if export_format == "rich":
        return data
    raise ValueError(f"Unknown export format: {export_format}")


class DatasetBuilder:
    def __init__(self, seed: int = 42, export_format: str = 'clean') -> None:
        self.seed = seed
        self.export_format = export_format
        self.samples: list[Sample] = []

    def add_samples(self, samples: list[Sample]) -> None:
        self.samples.extend(samples)

    def dedupe(self) -> None:
        seen: dict[tuple[str, str, str], Sample] = {}
        for sample in self.samples:
            key = (sample.module_id, sample.instruction, sample.input)
            seen[key] = sample
        self.samples = list(seen.values())

    def shuffle(self) -> None:
        random.Random(self.seed).shuffle(self.samples)

    def write_jsonl(self, output_path: str) -> Path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8') as handle:
            for sample in self.samples:
                row = json.dumps(_sample_to_dict(sample, export_format=self.export_format), ensure_ascii=False)
                handle.write(row + '\n')
        return path

    def summary(self) -> dict[str, object]:
        by_module = Counter(sample.module_id for sample in self.samples)
        by_difficulty = Counter(sample.difficulty for sample in self.samples)
        return {
            'seed': self.seed,
            'export_format': self.export_format,
            'sample_count': len(self.samples),
            'modules': dict(sorted(by_module.items())),
            'difficulty_counts': dict(sorted(by_difficulty.items())),
        }
