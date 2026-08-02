from shared.clear_thought.formatting import format_json
from shared.clear_thought.math_utils import normalize
from shared.clear_thought.validation import validate_session_data


def test_validate() -> None:
    assert validate_session_data({"thoughts": []})
    assert not validate_session_data({})


def test_format() -> None:
    assert "\n" in format_json({"a": 1})


def test_normalize() -> None:
    assert normalize(5, 0, 10) == 0.5  # noqa: PLR2004
    assert normalize(5, 5, 5) == 0.0
