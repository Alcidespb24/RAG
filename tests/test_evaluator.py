from rag.evaluator import evaluate_answers


def test_evaluate_answers_computes_expected_summary_metrics() -> None:
    expected = {
        "q1": "Answer with number 42 (Page 10)",
        "q2": "Answer without number",
    }
    predicted = {
        "q1": "Answer with number 42 (Page 10)",
        "q2": "totally different",
    }

    summary = evaluate_answers(expected=expected, predicted=predicted)

    assert summary.total_questions == 2
    assert summary.page_accuracy == 0.5
    assert summary.number_accuracy == 1.0
    assert 0 <= summary.average_term_coverage <= 1


def test_missing_prediction_is_treated_as_empty_response() -> None:
    expected = {"q1": "A health plan with annual receipts of $5 million or less. (Page 16)"}
    predicted = {}

    summary = evaluate_answers(expected=expected, predicted=predicted)

    assert summary.total_questions == 1
    assert summary.results[0].predicted_answer == ""
    assert summary.results[0].page_match is False
    assert summary.results[0].numbers_match is False
    assert summary.results[0].term_coverage == 0.0
