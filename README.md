# Retinoblastoma Detection

A framework-neutral skeleton for a supervised-learning retinoblastoma detection
project. The dataset format, labels, model family (CNN or SNN), and training
framework have not been selected yet.

## Project layout

- `data/`: dataset placeholder and notes; do not commit private or restricted
  medical data.
- `models/`: placeholders for future CNN and SNN implementations.
- `src/retinoblastoma_detection/`: reusable project code, dataset split
  container, and model-independent training/testing contracts.
- `tests/`: automated tests for the project skeleton.
- `training/` and `testing/`: entry-point placeholders for future workflows.

## Setup

Use Python 3.10 or later. Create a project-local environment with the Python
version selected for this project (the example uses Python 3.12):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

Run the skeleton tests:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Using the environment's Python executable explicitly avoids relying on whichever
Python version happens to be first on `PATH`.

## Dataset and evaluation notes

Dataset ingestion and label definitions are intentionally not implemented.
Document the source, permissions, label schema, and preprocessing when these
are decided. Define train, validation, and test splits before fitting; where
patient identifiers are available, keep each patient's data in only one split
to avoid leakage. Establish clinically appropriate evaluation metrics and
review procedures before using any results.

## Training and testing

`training/train.py` and `testing/test.py` are placeholders. The package
contracts in `src/retinoblastoma_detection/` provide generic split forwarding
to a future training or evaluation implementation without selecting a model
library or architecture.
