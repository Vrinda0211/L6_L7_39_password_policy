import pytest

from lab6.password_policy import check_password, strength, suggest_fix


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("Abcdef1!", []),
        ("Aa1!bcde" + "x" * 56, []),
    ],
)
def test_passwords_at_supported_length_boundaries(password, expected):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("Aa1!bcd", ["too short"]),
        ("Aa1!bcd" + "x" * 58, ["too long"]),
    ],
)
def test_passwords_outside_supported_length_range(password, expected):
    assert check_password(password) == expected


def test_common_password_matching_ignores_case():
    assert check_password("PASSWORD") == [
        "common",
        "no lowercase",
        "no digit",
        "no special",
    ]


def test_character_categories_accept_unicode_letters_and_symbols():
    assert check_password("Élan2026💡") == []


def test_strength_changes_at_fourteen_characters():
    assert strength("Abcdefgh1!XYZ") == "good"
    assert strength("Abcdefgh1!XYZq") == "strong"


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("A1!", "weak"),
        ("abc", "very weak"),
    ],
)
def test_strength_uses_the_number_of_policy_issues(password, expected):
    assert strength(password) == expected


@pytest.mark.parametrize(
    ("issues", "expected"),
    [
        ([], "none needed"),
        (["too short", "no lowercase"], "add more characters"),
        (["common", "no digit"], "avoid common passwords"),
        (["no uppercase"], "add uppercase"),
        (["too long"], "shorten it"),
    ],
)
def test_suggest_fix_selects_the_first_actionable_issue(issues, expected):
    assert suggest_fix(issues) == expected
