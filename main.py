from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from rag.evaluator import evaluate_answers
from rag.io import load_qa_map


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate RAG answers against a ground-truth dataset."
    )
    parser.add_argument(
        "--expected",
        default="data_source/truth_dataset.json",
        help="Path to ground-truth Q&A JSON file.",
    )
    parser.add_argument(
        "--predicted",
        default="data_source/sample_predictions.json",
        help="Path to model predictions Q&A JSON file.",
    )
    parser.add_argument(
        "--output",
        default="evaluation_results/latest_evaluation.json",
        help="Where to write machine-readable evaluation output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    expected = load_qa_map(args.expected)
    predicted = load_qa_map(args.predicted)

    summary = evaluate_answers(expected=expected, predicted=predicted)

    print("RAG Evaluation Summary")
    print("-" * 24)
    print(f"Questions: {summary.total_questions}")
    print(f"Page accuracy: {summary.page_accuracy:.1%}")
    print(f"Number accuracy: {summary.number_accuracy:.1%}")
    print(f"Average term coverage: {summary.average_term_coverage:.1%}")

    payload = {
        "total_questions": summary.total_questions,
        "page_accuracy": summary.page_accuracy,
        "number_accuracy": summary.number_accuracy,
        "average_term_coverage": summary.average_term_coverage,
        "results": [
            {
                "question": result.question,
                "expected_answer": result.expected_answer,
                "predicted_answer": result.predicted_answer,
                "page_match": result.page_match,
                "numbers_match": result.numbers_match,
                "term_coverage": result.term_coverage,
            }
            for result in summary.results
        ],
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Saved detailed results to {output_path}")


if __name__ == "__main__":
    main()
