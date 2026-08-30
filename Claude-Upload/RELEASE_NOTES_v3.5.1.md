# SIMS Writer Claude v3.5.1 Release Notes

Date: 2026-08-30

## Fix

- Windows Explorer extraction error `0x80010135` (path too long) is prevented by distributing the ZIP without a redundant product-name top-level folder.
- Distribution caches such as `.pytest_cache`, `__pycache__`, and `.pyc` are excluded.
- No Writer diagnosis/editing logic, JSON contract, or Personal Knowledge candidate behavior is changed from v3.5.0.

## Distribution rule

The ZIP root now contains the package files directly. This avoids duplicating the long product name when Windows creates an extraction destination folder from the ZIP filename.
