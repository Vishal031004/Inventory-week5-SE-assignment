"# Inventory-week5-SE-assignment" 

| Issue | Line(s) | Type | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Use of `eval`** | 59 | Security (Bandit) | `[B307:blacklist]` Use of possibly insecure function. `eval()` can run any code, which is a major vulnerability. | Replace the `eval(...)` call with a simple `print()` statement. |
| **Dangerous Default Value** | 8 | Bug (Pylint) | `W0102:` Dangerous default value `[]` as argument. The `logs` list will be shared across all calls to `addItem`. | Change the default to `None` and then initialize `logs = []` inside the function if it's `None`, just like the lab example. |
| **Bare `except`** | 19 | Bug (Pylint/Flake8) | `E722:` do not use bare 'except'. This catches all errors, including `SystemExit`, making the code dangerous and hard to debug. | Replace the bare `except:` with the specific error you expect, which is `except KeyError:`. |
| **Unused Import** | 2 | Style (Flake8/Pylint) | `F401:` 'logging' imported but unused. The `logging` module is imported but never used, adding clutter. | Delete the entire line `import logging`. |