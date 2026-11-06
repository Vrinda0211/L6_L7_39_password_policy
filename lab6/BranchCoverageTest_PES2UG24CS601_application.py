import pytest

from lab6.password_policy import check_password, strength, suggest_fix


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("", ["too short", "no uppercase", "no lowercase", "no digit", "no special"]),
        ("Aa1!abc", ["too short"]),
        ("Aa1!abcd", []),
        ("Aa1!bcde" + "z" * 56, []),
        ("Aa1!bcde" + "z" * 57, ["too long"]),
    ],
)
def test_length_decision_outcomes_and_empty_input(password, expected):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("letmein", ["too short", "common", "no uppercase", "no digit", "no special"]),
        ("L3tMeIn!", []),
        ("aB2!", ["too short"]),
        ("Abcd1234", ["no special"]),
        ("Abcd!@#$", ["no digit"]),
    ],
)
def test_common_password_and_character_class_decisions(password, expected):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("Abcdefgh1!XY", "good"),
        ("Abcdefgh1!XYZ", "good"),
        ("Abcdefgh1!XYZq", "strong"),
        ("A1!", "weak"),
        ("abc", "very weak"),
    ],
)
def test_strength_decision_thresholds(password, expected):
    assert strength(password) == expected


@pytest.mark.parametrize(
    ("issues", "expected"),
    [
        ([], "none needed"),
        (["too short"], "add more characters"),
        (["common"], "avoid common passwords"),
        (["no special"], "add special"),
        (["too long"], "shorten it"),
    ],
)
def test_suggestion_decision_outcomes(issues, expected):
    assert suggest_fix(issues) == expected
