from __future__ import annotations

import re
from dataclasses import dataclass


_WORD_RE = re.compile(r"\b[\w$./-]+\b")
_PAGE_RE = re.compile(r"\bpage\s*(\d+)\b", re.IGNORECASE)
_NUMBER_RE = re.compile(r"\d+(?:\.\d+)?")


@dataclass(slots=True)
class EvaluationResult:
    question: str
    expected_answer: str
    predicted_answer: str
    page_match: bool
    numbers_match: bool
    term_coverage: float


@dataclass(slots=True)
class EvaluationSummary:
    total_questions: int
    page_accuracy: float
    number_accuracy: float
    average_term_coverage: float
    results: list[EvaluationResult]


def _extract_page(text: str) -> str | None:
    match = _PAGE_RE.search(text)
    return match.group(1) if match else None


def _extract_numbers(text: str) -> set[str]:
    return set(_NUMBER_RE.findall(text))


def _tokenize(text: str) -> set[str]:
    return {token.lower() for token in _WORD_RE.findall(text)}


def _term_coverage(expected: str, predicted: str) -> float:
    expected_terms = _tokenize(expected)
    if not expected_terms:
        return 1.0

    predicted_terms = _tokenize(predicted)
    overlap = expected_terms.intersection(predicted_terms)
    return len(overlap) / len(expected_terms)


def evaluate_answers(expected: dict[str, str], predicted: dict[str, str]) -> EvaluationSummary:
    results: list[EvaluationResult] = []

    for question, expected_answer in expected.items():
        predicted_answer = predicted.get(question, "")
        expected_page = _extract_page(expected_answer)
        predicted_page = _extract_page(predicted_answer)

        result = EvaluationResult(
            question=question,
            expected_answer=expected_answer,
            predicted_answer=predicted_answer,
            page_match=expected_page is not None and expected_page == predicted_page,
            numbers_match=_extract_numbers(expected_answer).issubset(_extract_numbers(predicted_answer)),
            term_coverage=_term_coverage(expected_answer, predicted_answer),
        )
        results.append(result)

    total = len(results)
    if total == 0:
        return EvaluationSummary(0, 0.0, 0.0, 0.0, [])

    page_accuracy = sum(result.page_match for result in results) / total
    number_accuracy = sum(result.numbers_match for result in results) / total
    average_term_coverage = sum(result.term_coverage for result in results) / total

    return EvaluationSummary(
        total_questions=total,
        page_accuracy=page_accuracy,
        number_accuracy=number_accuracy,
        average_term_coverage=average_term_coverage,
        results=results,
    )
