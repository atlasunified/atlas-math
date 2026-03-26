# Atlas Math Evaluation (2026-03-26)

## Scope

This evaluation reviews whether Atlas Math can generate math problems reliably and whether the implementation quality is production-ready.

## What I ran

1. `python main.py list`
2. `python main.py build --size small --format clean --output /tmp/atlas-small.jsonl`
3. `python main.py build --modules algebra.equations.one_step --target-records 200 --output /tmp/one-step.jsonl`
4. `python main.py build --size small --format clean --output /tmp/atlas-small-after.jsonl`

## Findings

### Problem generation ability

- The project discovers a large catalog of generator modules and can build datasets through the CLI.
- A small mixed build produced 92 unique rows in this environment, which demonstrates practical generation works.
- For a focused module (`algebra.equations.one_step`), a 200-target run produced 196 unique rows in one round after the bug fix below.

### Code quality observations

**Strengths**

- Registry-driven design and metadata-based module discovery make extension straightforward.
- Structured generation hooks (`generate_unique`, `iter_samples`) and post-hoc dedupe are useful for dataset quality control.
- Type-hinted dataclasses and shared serialization paths keep the output shape consistent.

**Weaknesses / risks**

- No formal test suite was found in the repository, which increases regression risk.
- Runtime errors in a single module can silently reduce dataset yield (`[skip] ...`) rather than fail fast.
- Achieving exact target sizes is not guaranteed because duplicate-heavy rounds can stall before target tolerance.

## Fix applied during evaluation

In `algebra.equations.one_step`, the division branch computed `rhs = sol / k`, which becomes a `float` for integer `sol` values at lower difficulties. The formatter expects fraction-like objects with `.numerator` and `.denominator`, causing occasional runtime skips.

I changed this to `rhs = Fraction(sol, k)` so generated RHS values are always fraction-safe and formatting-compatible.

## Conclusion

- **Ability to generate problems:** Good. The generator framework is broad and functional.
- **Code quality:** Fair-to-good, but not yet “high-assurance” due to missing automated tests and partial-failure behavior.
- **Recommendation:** Add automated module-level validation tests and fail-on-error CI mode before calling it fully robust.
