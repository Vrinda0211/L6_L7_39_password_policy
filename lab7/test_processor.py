from hypothesis import given, strategies as st

from processor import digit_ratio, first_character_type, split_credentials


invalid_scalar_inputs = st.one_of(
    st.none(),
    st.integers(),
    st.booleans(),
)


@given(st.text(min_size=1))
def test_first_character_type_classifies_nonempty_text(value):
    first_character = value[0]

    if first_character.isdigit():
        expected = "digit"
    elif first_character.isalpha():
        expected = "letter"
    else:
        expected = "symbol"

    assert first_character_type(value) == expected


@given(st.one_of(invalid_scalar_inputs, st.just("")))
def test_first_character_type_handles_invalid_inputs(value):
    assert first_character_type(value) is None


@given(
    st.tuples(
        st.text(alphabet=st.characters(blacklist_characters=":")),
        st.text(alphabet=st.characters(blacklist_characters=":")),
    )
)
def test_split_credentials_splits_one_separator(credentials):
    user, password = credentials

    assert split_credentials(f"{user}:{password}") == (
        user.strip(),
        password.strip(),
    )


@given(
    st.one_of(
        invalid_scalar_inputs,
        st.text().filter(lambda value: value.count(":") != 1),
    )
)
def test_split_credentials_handles_invalid_inputs(value):
    assert split_credentials(value) is None


@given(st.text(min_size=1))
def test_digit_ratio_is_the_fraction_of_digit_characters(value):
    expected = sum(character.isdigit() for character in value) / len(value)

    assert digit_ratio(value) == expected
    assert 0.0 <= digit_ratio(value) <= 1.0


@given(st.one_of(invalid_scalar_inputs, st.just("")))
def test_digit_ratio_handles_invalid_inputs(value):
    assert digit_ratio(value) == 0.0
