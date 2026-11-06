# L6_L7_39 — Password Policy Checker

Lab 7: Fuzz Testing

## About

A small Python module that classifies the first password character, splits credentials and measures digit density.

## Files

| File | Description |
|------|-------------|
| `processor.py` | The application and functions under test |
| `test_processor.py` | Hypothesis property-based tests |
| `Lab_7_FuzzTesting_Student_Handout.pdf` | Official lab requirements |
| `screenshots/` | Terminal evidence from the original, failing and fixed runs |

Invalid inputs return `None` from `first_character_type` and `split_credentials`, and `0.0` from `digit_ratio`. Valid input behavior is unchanged.

Run the application and tests from this directory:

```text
python processor.py
python -m pytest test_processor.py -v
```
