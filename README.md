# Atlas Math

Atlas Math is a synthetic mathematics dataset generation toolkit and the current home of the AtlasUnified math generation codebase.

It provides:

- Python generators for large-scale math problem creation
- CLI tooling to build JSONL datasets
- controllable topic, difficulty, and output formats
- a companion public dataset on Hugging Face: `AtlasUnified/atlas-math-sets`

## Repository status

This repository, `atlasunified/atlas-math`, is the current repository.

Earlier AtlasUnified math repositories are predecessors, including:

- `atlasunified/atlas-mathematical-computations`

## Dataset

The companion dataset is published at:

- `AtlasUnified/atlas-math-sets`

At the time of writing, the dataset page reports:

- 22,259,474 total rows
- train: 17.8M rows
- validation: 2.23M rows
- test: 2.23M rows
- downloaded dataset size: 3.49 GB
- auto-converted Parquet size: 1.69 GB
- license: MIT

The dataset is organized around four core fields:

```json
{
  "answer": "[num]",
  "input": "[equation]",
  "output": "[num]",
  "instruction": "[pre-generated_instruction] [equation]"
}
```

Example:

```json
{
  "instruction": "Sum up 98296 + 65243",
  "input": "98296 + 65243",
  "output": "98296 + 65243 = 163539",
  "answer": "163539"
}
```

## What Atlas Math provides

The codebase includes:

- a registry-driven generator framework
- command-line dataset building tools
- interactive generation flows
- dataset export utilities
- modular topic-based generators
- configurable deduplication and retry logic
- multiple dataset output formats

Based on the current source structure available here, the generator library spans six top-level topics:

- algebra
- prealgebra
- geometry
- trigonometry
- statistics
- calculus

## Repository layout

```text
atlas_math/
├── cli.py
├── cli_commands.py
├── cli_generation.py
├── cli_interactive.py
├── cli_dashboard.py
├── dataset_builder.py
├── registry.py
├── schemas.py
├── modules/
│   ├── algebra/
│   ├── prealgebra/
│   ├── geometry/
│   ├── trigonometry/
│   ├── statistics/
│   └── calculus/
└── utils/
```

Top-level repository files include:

```text
atlas_math/
LICENSE
README.md
__init__.py
constants.py
main.py
```

## Installation

```bash
git clone https://github.com/atlasunified/atlas-math.git
cd atlas-math
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

If you add packaging metadata later, you can extend this section with `pip install -e .` or requirements-based installation.

## Quick start

### List available modules

```bash
python main.py list
```

### List modules as JSON

```bash
python -m atlas_math.cli list --json
```

### Build a small dataset

```bash
python main.py build \
  --size small \
  --format clean \
  --output outputs/atlas-math-small.jsonl
```

### Build a topic-specific dataset

```bash
python main.py build \
  --topic algebra \
  --size medium \
  --difficulty-mix balanced \
  --generation-mode auto \
  --progress \
  --output outputs/algebra-medium.jsonl
```

### Build with an exact record target

```bash
python main.py build \
  --topics algebra geometry statistics \
  --target-records 25000 \
  --difficulty-mix curriculum \
  --dedupe-mode input_answer \
  --max-rounds 4 \
  --output outputs/custom-25k.jsonl
```

## CLI overview

### `list`

```bash
python main.py list [--json]
```

This command enumerates discovered generator modules.

### `build`

```bash
python main.py build \
  [--topic TOPIC] \
  [--topics TOPIC [TOPIC ...]] \
  [--modules MODULE_ID [MODULE_ID ...]] \
  [--size {small,medium,large,full}] \
  [--target-records N] \
  [--difficulty-mix {balanced,curriculum,advanced,middle_heavy}] \
  [--generation-mode {auto,structured,random}] \
  [--format {clean,extended,rich}] \
  [--output PATH] \
  [--progress] \
  [--dedupe-mode {input_answer,input_only,full}] \
  [--workers N] \
  [--max-batch-size N] \
  [--min-yield-ratio FLOAT] \
  [--exhaustion-patience N] \
  [--target-tolerance FLOAT] \
  [--max-rounds N]
```

## Size presets

The current CLI defines these presets:

- `small`: 100
- `medium`: 1,000
- `large`: 5,000
- `full`: 20,000

## Difficulty mixes

Built-in difficulty mixes include:

- `balanced`
- `curriculum`
- `advanced`
- `middle_heavy`

## Output formats

### `clean`

A minimal format suitable for training pipelines.

```json
{
  "instruction": "Solve the equation x + 5 = 12.",
  "input": "x + 5 = 12",
  "answer": "7",
  "answer_words": "seven",
  "difficulty": "level_1"
}
```

### `extended`

Adds topic-level metadata.

```json
{
  "instruction": "Solve the equation x + 5 = 12.",
  "input": "x + 5 = 12",
  "answer": "7",
  "answer_words": "seven",
  "difficulty": "level_1",
  "topic": "algebra",
  "subtopic": "equations.one_step"
}
```

### `rich`

Preserves the full serialized sample, including generated output text, module identifiers, and metadata.

## Interactive mode

Running the tool without a subcommand opens an interactive workflow for:

- browsing registered modules
- selecting topics or modules
- choosing preset or custom sizes
- setting difficulty mix and generation mode
- configuring workers, tolerance, and retry limits
- writing output directly to JSONL

```bash
python main.py
```

## How generation works

A typical build pipeline:

1. discovers enabled modules through the registry
2. resolves topic and module selections
3. allocates targets across difficulty buckets
4. generates samples, optionally with multiprocessing
5. applies duplicate filtering
6. retries underfilled buckets when necessary
7. writes final JSONL output

When modules expose structured interfaces such as `generate_unique`, `iter_unique`, or `iter_samples`, the builder can use them directly. Otherwise it falls back to random generation.

## Example topic coverage

Example generator categories present in the source tree include:

- algebra equations and systems
- decimal and fraction conversion
- geometry measurement and relations
- trigonometric identities and applications
- statistics tables and interpretation
- calculus applications

## Loading the published dataset

### Hugging Face Datasets

```python
from datasets import load_dataset

ds = load_dataset("AtlasUnified/atlas-math-sets")
print(ds)
print(ds["train"][0])
```

### Streaming

```python
from datasets import load_dataset

stream = load_dataset("AtlasUnified/atlas-math-sets", split="train", streaming=True)
first = next(iter(stream))
print(first)
```

## Recommended use cases

- supervised fine-tuning for math instruction following
- arithmetic and symbolic reasoning benchmarks
- curriculum-based training by difficulty band
- synthetic data augmentation
- generator evaluation and deduplication testing

## Notes on `answer` vs `output`

The published dataset uses both fields:

- `answer` is the final answer string
- `output` is the rendered computation or formatted result string

Example:

```json
{
  "input": "895424 * 550843",
  "output": "895424 x 550843 = 493238042432",
  "answer": "493238042432",
  "instruction": "Could you please multiply 895424 * 550843"
}
```

This distinction is useful when training either concise-answer systems or formatted-solution systems.

## License

This repository uses the MIT License. The companion dataset page also lists MIT.

## Citation

```bibtex
@misc{atlas_math,
  title        = {Atlas Math},
  author       = {AtlasUnified},
  howpublished = {GitHub repository and Hugging Face dataset},
  year         = {2026},
  note         = {Synthetic mathematics generation toolkit and dataset}
}
```
