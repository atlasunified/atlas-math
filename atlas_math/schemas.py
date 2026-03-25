from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class Sample:
    module_id: str
    topic: str
    subtopic: str
    difficulty: str
    difficulty_level: int
    instruction: str
    input: str
    output: str
    output_words: str
    answer: str
    answer_words: str
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(slots=True)
class ModuleInfo:
    module_id: str
    name: str
    topic: str
    subtopic: str
    tags: list[str]
    description: str
    difficulty_levels: list[str]
    enabled: bool = True
