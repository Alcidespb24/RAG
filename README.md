# HIPAA RAG Evaluation Toolkit

A clean, recruiter-friendly Python project that demonstrates how to **evaluate Retrieval-Augmented Generation (RAG)** quality on a domain dataset.

This repository focuses on **evaluation engineering**: loading Q&A datasets, scoring model answers with transparent metrics, and producing reproducible outputs.

## Why this project matters

- Shows practical RAG evaluation skills beyond prompting.
- Includes reusable Python modules instead of notebook-only logic.
- Produces machine-readable results for automation and reporting.
- Comes with tests for core metric behavior.

## What is evaluated

Given:
- an **expected** answer set (`question -> gold answer`), and
- a **predicted** answer set (`question -> model answer`),

the toolkit computes:

1. **Page accuracy**: whether cited page numbers match.
2. **Number accuracy**: whether expected numeric values appear in the prediction.
3. **Term coverage**: lexical overlap between expected and predicted terms.

## Project structure

```text
RAG/
├── data_source/
│   ├── hipaa-simplification-201303.pdf
│   ├── truth_dataset.json
│   └── sample_predictions.json
├── src/rag/
│   ├── __init__.py
│   ├── evaluator.py
│   └── io.py
├── tests/
│   └── test_evaluator.py
├── main.py
└── pyproject.toml
```

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -e .[dev]
python main.py
```

### Example output

```text
RAG Evaluation Summary
------------------------
Questions: 5
Page accuracy: 20.0%
Number accuracy: 40.0%
Average term coverage: 76.8%
Saved detailed results to evaluation_results/latest_evaluation.json
```

## Run tests

```bash
pytest
```

## Recruiter notes

This project demonstrates:
- modular Python packaging (`src/` layout),
- CLI design with argument parsing,
- deterministic evaluation logic,
- unit testing of metric calculations,
- clean documentation and reproducible results.
