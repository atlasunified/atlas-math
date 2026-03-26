# Atlas Mathematical Computations

Synthetic large-scale mathematical computation generators and a matching public dataset for training, evaluation, and benchmarking.

- **Repository:** `atlasunified/atlas-mathematical-computations`
- **Dataset:** `AtlasUnified/atlas-math-sets`
- **License:** MIT

This project contains Python generators for math problem creation plus CLI tooling to build JSONL datasets with controllable size, difficulty, topic coverage, and deduplication. The companion Hugging Face dataset currently exposes **22,259,474 rows** across **train / validation / test** splits, with JSON records built around `instruction`, `input`, `output`, and `answer`. See the dataset card for the published counts and field layout. citeturn196616view2turn196616view3turn196616view5

## What this repo provides

The codebase is more than a handful of arithmetic scripts: it includes a registry-driven generator framework, a CLI, an interactive builder, dataset export utilities, and hundreds of topic modules discovered from `atlas_math.modules`. The uploaded source dump shows:

- a **global module registry** that auto-discovers enabled generator modules by `MODULE_INFO`
- a CLI with `list` and `build` commands
- output formats: `clean`, `extended`, and `rich`
- post-hoc deduplication modes: `input_answer`, `input_only`, and `full`
- difficulty controls spanning `level_1` to `level_5`
- retry logic, yield estimation, multi-process generation, and an ANSI dashboard
- a `Sample` schema with fields including `instruction`, `input`, `output`, `answer`, difficulty metadata, and per-sample metadata fileciteturn2file1L1-L52 fileciteturn2file3L14-L39 fileciteturn1file0L1-L111

From the uploaded source export, the current generator library contains **308 modules** across **6 top-level topics**:

- algebra
- prealgebra
- geometry
- trigonometry
- statistics
- calculus

That module/topic coverage comes from the repository source export provided in this chat. fileciteturn0file0

## Published dataset

The public dataset page describes **ATLAS MATH SETS** as mathematical computation data derived from Python scripts, including addition, subtraction, multiplication, division, fractions, decimals, square roots, cube roots, exponents, and factors. The dataset viewer shows:

- **22.3M rows total**
- **train:** 17.8M rows
- **validation:** 2.23M rows
- **test:** 2.23M rows
- **downloaded dataset size:** 3.49 GB
- **auto-converted Parquet size:** 1.69 GB
- modalities: text
- format: json
- language: English
- task tag: question answering citeturn196616view2turn196616view3turn196616view5

### Dataset record format

The dataset card states the JSONL format as:

```json
{"answer":"[num]","input":"[equation]","output":"[num]","instruction":"[pre-generated_instruction] [equation]"}
```

The dataset viewer examples confirm the same four core fields and show examples such as:

- `input`: `98296 + 65243`
- `output`: `98296 + 65243 = 163539`
- `answer`: `163539`
- `instruction`: `Sum up 98296 + 65243` citeturn196616view3turn196616view5turn196616view6

## Repository architecture

```text
atlas_math/
├── cli.py                  # CLI entrypoint
├── cli_commands.py         # list/build command definitions
├── cli_generation.py       # planning, multiprocessing, retries, dedupe
├── cli_interactive.py      # interactive builder
├── cli_dashboard.py        # terminal progress dashboard
├── dataset_builder.py      # dataset export utilities
├── registry.py             # auto-discovery of generator modules
├── schemas.py              # Sample / ModuleInfo dataclasses
├── modules/
│   ├── algebra/
│   ├── prealgebra/
│   ├── geometry/
│   ├── trigonometry/
│   ├── statistics/
│   └── calculus/
└── utils/
```

The CLI entrypoint dispatches to `list` and `build`, and falls back to an interactive menu when no subcommand is supplied. fileciteturn1file0L17-L111

## Installation

```bash
git clone https://github.com/atlasunified/atlas-mathematical-computations.git
cd atlas-mathematical-computations
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

This repository appears to rely mainly on the Python standard library in the uploaded source export. If you later add packaging metadata or a requirements file, update this section accordingly. fileciteturn0file0

## Quick start

### List available modules

```bash
python main.py list
```

or

```bash
python -m atlas_math.cli list --json
```

The `list` command prints discovered modules and can emit JSON with module id, name, topic, difficulty levels, and whether a module supports structured generation. fileciteturn1file0L17-L52

### Build a small dataset

```bash
python main.py build   --size small   --format clean   --output outputs/atlas-math-small.jsonl
```

### Build a topic-specific dataset

```bash
python main.py build   --topic algebra   --size medium   --difficulty-mix balanced   --generation-mode auto   --progress   --output outputs/algebra-medium.jsonl
```

### Build with an exact target size

```bash
python main.py build   --topics algebra geometry statistics   --target-records 25000   --difficulty-mix curriculum   --dedupe-mode input_answer   --max-rounds 4   --output outputs/custom-25k.jsonl
```

## CLI reference

### `list`

```bash
python main.py list [--json]
```

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

### Size presets

The repository defines the following presets:

- `small` = 100
- `medium` = 1,000
- `large` = 5,000
- `full` = 20,000 fileciteturn1file0L112-L198

### Difficulty mixes

The repository includes these built-in mixes:

- `balanced`
- `curriculum`
- `advanced`
- `middle_heavy` fileciteturn1file0L112-L198

### Output formats

#### `clean`
Minimal records for model training:

```json
{
  "instruction": "Solve the equation x + 5 = 12.",
  "input": "x + 5 = 12",
  "answer": "7",
  "answer_words": "seven",
  "difficulty": "level_1"
}
```

#### `extended`
Adds topic metadata:

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

#### `rich`
Preserves the full serialized sample, including module ids, output text, and metadata. Serialization logic for these formats is defined in the CLI helpers. fileciteturn1file0L112-L198

## Interactive mode

Running the tool without a subcommand opens an interactive menu that lets you:

1. list registered modules
2. choose one or more topics
3. select a preset or custom target size
4. choose a difficulty mix and generation mode
5. set workers, tolerance, and retry rounds
6. build directly to a JSONL output path fileciteturn1file0L1-L16 fileciteturn1file0L199-L400

```bash
python main.py
```

## How generation works

The generator pipeline:

1. discovers enabled modules through the registry
2. expands selected topics into module ids
3. allocates targets across difficulty buckets
4. generates raw records with multiprocessing
5. tracks local and global duplicates
6. retries under-producing buckets when needed
7. writes the final deduplicated JSONL output

The build planner also supports structured generation when modules expose `generate_unique`, `iter_unique`, or `iter_samples`, and falls back to random generation otherwise. fileciteturn2file1L1-L52 fileciteturn1file0L112-L198

## Example generator modules

The uploaded source export shows generators ranging from simple arithmetic to higher-level math, for example:

- one-step, two-step, and multi-step algebra equations
- equation special cases
- trigonometric identities and applications
- statistics table problems
- calculus fundamental theorem items

Each module declares `MODULE_INFO`, difficulty levels, instruction templates, and a `generate` method. fileciteturn1file0L1-L111 fileciteturn1file3L1-L62 fileciteturn1file4L1-L55 fileciteturn2file4L1-L87

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
- curriculum-style training by difficulty band
- synthetic data augmentation
- evaluation of deduplication and generation pipelines

## Notes on `answer` vs `output`

The public dataset uses both `answer` and `output`:

- `answer` is the final answer string
- `output` is the rendered computation or worked result string

Example:

```json
{
  "input": "895424 * 550843",
  "output": "895424 x 550843 = 493238042432",
  "answer": "493238042432",
  "instruction": "Could you please multiply 895424 * 550843"
}
```

This distinction is visible in the dataset viewer and is useful for training either concise-answer or formatted-output tasks. citeturn196616view5

## License

Both the GitHub repository and the Hugging Face dataset page indicate **MIT** licensing. citeturn848035view0turn196616view2

## Citation

```bibtex
@misc{atlas_math_sets,
  title        = {ATLAS Math Sets},
  author       = {AtlasUnified},
  howpublished = {Hugging Face dataset and GitHub repository},
  year         = {2026},
  note         = {Synthetic mathematical computation dataset and generation framework}
}
```

## Acknowledgment

This README was aligned to the current repository source exported in the uploaded file rather than only the older short GitHub landing README, so it reflects the present CLI and module architecture more accurately. fileciteturn0file0
