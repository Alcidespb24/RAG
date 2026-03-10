from __future__ import annotations

import json
from pathlib import Path


def load_qa_map(path: str | Path) -> dict[str, str]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"Expected a JSON object in {path}, got {type(raw).__name__}")

    qa_map = {str(question).strip(): str(answer).strip() for question, answer in raw.items()}
    if not qa_map:
        raise ValueError(f"No questions found in {path}")

    return qa_map
