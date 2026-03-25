from __future__ import annotations

import random
import re
from typing import Any, Callable, Iterable, Sequence

from atlas_math.schemas import Sample
from atlas_math.utils import number_words

DIFFICULTIES = ["level_1", "level_2", "level_3", "level_4", "level_5"]
LEVELS = DIFFICULTIES
DIFF_TO_LEVEL = {d: i + 1 for i, d in enumerate(DIFFICULTIES)}
DIFFICULTY_TO_LEVEL = dict(DIFF_TO_LEVEL)


def sample_count_from_count(count: int | None) -> int:
    if count is None:
        return 10
    return max(1, int(count))


def capacity(*args, **kwargs) -> None:
    return None


def rng_from_seed(seed: int | None = None) -> random.Random:
    return random.Random(seed)


def pick(rng: random.Random, seq: Sequence[Any]) -> Any:
    if not seq:
        raise ValueError("pick() cannot choose from an empty sequence")
    return rng.choice(list(seq))


def bounded_int(
    rng: random.Random,
    lo: int,
    hi: int,
    exclude: set[int] | None = None,
    *,
    nonzero: bool = False,
) -> int:
    blocked = set(exclude or set())
    if nonzero:
        blocked.add(0)
    while True:
        value = rng.randint(lo, hi)
        if value not in blocked:
            return value


def nzint(rng: random.Random, a: int = -9, b: int = 9, exclude: set[int] | None = None) -> int:
    return bounded_int(rng, a, b, exclude=exclude, nonzero=True)


def signed_int(rng: random.Random, low: int, high: int, exclude_zero: bool = False) -> int:
    return bounded_int(rng, low, high, nonzero=exclude_zero)


def int_words(n: int) -> str:
    return number_words(int(n))


def choose_instruction(rng: random.Random, *args: object) -> str:
    if len(args) == 1:
        return str(args[0])
    if len(args) == 2:
        instructions, problem = args
        choices = list(instructions) if isinstance(instructions, (list, tuple)) else []
        if not choices:
            return str(problem)
        opener = rng.choice(choices)
        return f"{opener} {problem}" if opener else str(problem)
    raise TypeError("choose_instruction() expects (rng, problem) or (rng, instructions, problem)")


def choose_template(
    rng: random.Random,
    templates: list[str] | tuple[str, ...],
    problem: str | None = None,
) -> str:
    template = rng.choice(list(templates))
    return f"{template} {problem}" if problem else template


def re_full_int(s: str) -> bool:
    return bool(re.fullmatch(r"-?\d+", str(s).strip()))


def _coerce_numeric_words(value: str) -> str:
    text = str(value).strip()
    if re.fullmatch(r"-?\d+", text):
        try:
            return number_words(int(text))
        except Exception:
            return text
    if re.fullmatch(r"-?\d+\.\d+", text):
        try:
            return number_words(float(text))
        except Exception:
            return text
    return text


def _looks_like_single_assignment(text: str) -> bool:
    return "=" in text and text.count("=") == 1


def _answer_words(answer: str, explicit: str | None = None) -> str:
    if explicit is not None:
        return str(explicit)

    text = str(answer).strip()
    if _looks_like_single_assignment(text):
        lhs, rhs = [x.strip() for x in text.split("=", 1)]
        return f"{lhs} equals {_coerce_numeric_words(rhs)}"

    spoken = _coerce_numeric_words(text)
    return spoken


def expr_to_words(text: Any) -> str:
    return str(text)


number_to_words = int_words


def make_sample(*args, **kwargs) -> Sample:
    """
    Compatibility wrapper supporting both:
      old positional:
        make_sample(module_id, topic, subtopic, difficulty, instruction, input_text, answer, answer_words=None, metadata=None)
      new keyword-only:
        make_sample(module_id=..., topic=..., subtopic=..., difficulty=..., instruction=..., input_text=..., answer=..., metadata=..., answer_words=...)
    """
    answer_words = kwargs.pop("answer_words", None)
    metadata = kwargs.pop("metadata", None)

    if args:
        if len(args) < 7:
            raise TypeError("make_sample() positional form expects at least 7 arguments")
        module_id, topic, subtopic, difficulty, instruction, input_text, answer = args[:7]
        if len(args) >= 8 and answer_words is None:
            answer_words = args[7]
        if len(args) >= 9 and metadata is None:
            metadata = args[8]
    else:
        module_id = kwargs.pop("module_id")
        topic = kwargs.pop("topic")
        subtopic = kwargs.pop("subtopic")
        difficulty = kwargs.pop("difficulty")
        instruction = kwargs.pop("instruction")
        input_text = kwargs.pop("input_text", kwargs.pop("problem", kwargs.pop("input", "")))
        answer = kwargs.pop("answer")
        if metadata is None:
            metadata = kwargs.pop("metadata", {})
        if answer_words is None:
            answer_words = kwargs.pop("answer_words", None)

    if kwargs:
        unexpected = ", ".join(sorted(kwargs))
        raise TypeError(f"make_sample() got unexpected keyword arguments: {unexpected}")

    clean_answer = str(answer)
    spoken_answer = _answer_words(clean_answer, explicit=answer_words)
    difficulty_level = DIFFICULTY_TO_LEVEL.get(str(difficulty), 1)

    return Sample(
        module_id=str(module_id),
        topic=str(topic),
        subtopic=str(subtopic),
        difficulty=str(difficulty),
        difficulty_level=difficulty_level,
        instruction=str(instruction),
        input=str(input_text),
        output=clean_answer,
        output_words=spoken_answer,
        answer=clean_answer,
        answer_words=spoken_answer,
        metadata=dict(metadata or {}),
    )


def pick_unique(factory: Callable[[int], Sample], keys: Iterable[int]) -> list[Sample]:
    out: list[Sample] = []
    seen: set[tuple[str, str, str]] = set()
    for k in keys:
        sample = factory(k)
        sig = (sample.module_id, sample.instruction, sample.input)
        if sig in seen:
            continue
        seen.add(sig)
        out.append(sample)
    return out


def iter_from_generate(generate_fn, difficulty: str = "level_1", seed: int | None = None):
    rng = random.Random(seed)
    while True:
        batch_seed = rng.randint(0, 2**31 - 1)
        batch = generate_fn(count=1, difficulty=difficulty, seed=batch_seed)
        if not batch:
            return
        for sample in batch:
            yield sample
