"# Inventory-week5-SE-assignment" 


Issue Documentation Table :

| Issue | Line(s) | Type | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Use of `eval`** | 59 | Security (Bandit) | `[B307:blacklist]` Use of possibly insecure function. `eval()` can run any code, which is a major vulnerability. | Replace the `eval(...)` call with a simple `print()` statement. |
| **Dangerous Default Value** | 8 | Bug (Pylint) | `W0102:` Dangerous default value `[]` as argument. The `logs` list will be shared across all calls to `addItem`. | Change the default to `None` and then initialize `logs = []` inside the function if it's `None`, just like the lab example. |
| **Bare `except`** | 19 | Bug (Pylint/Flake8) | `E722:` do not use bare 'except'. This catches all errors, including `SystemExit`, making the code dangerous and hard to debug. | Replace the bare `except:` with the specific error you expect, which is `except KeyError:`. |
| **Unused Import** | 2 | Style (Flake8/Pylint) | `F401:` 'logging' imported but unused. The `logging` module is imported but never used, adding clutter. | Delete the entire line `import logging`. |




Reflection Questions :

1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest Issues: The simplest fixes involved the unused logging import and the eval() call. These were straightforward, single-line corrections (deletion or replacement) that required minimal analysis of the program's overall flow.

Hardest Issue: The most challenging issue was the mutable default argument (logs=[]). This is a semantic error requiring conceptual understanding of Python's function definition process. Fixing it required implementing the standard design pattern of using None as a sentinel value, which is more involved than a typical syntax correction.

2. Did the static analysis tools report any false positives? If so, describe one example.

No, the tools did not report any false positives regarding security or logical errors. All flagged high-priority issues (e.g., eval(), bare except:, mutable default) were valid flaws. The only warnings that could be considered debatable were stylistic conventions, such as Pylint's C0103 warning for function names not following the standard snake_case convention.

3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate the tools at two critical points:

Local Development: I would use pre-commit hooks to automatically run fast linters (like Flake8) before a commit is finalized. This ensures immediate feedback and prevents style or formatting errors from entering the repository.

Continuous Integration (CI) Pipeline: I would configure the CI service to run the full, comprehensive suite of tools (Pylint and Bandit) on every pull request. This serves as an automated quality gate, blocking the merge if high-severity security or logic issues are detected.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Robustness: The code is more reliable. Replacing the bare except: with except KeyError: ensures the error handling is precise, preventing the suppression of unrelated, critical system exceptions.

Security: Removing the eval() call eliminated a severe code injection vulnerability, critically improving the application's security posture.

Correctness: Fixing the mutable default argument ensures the addItem function behaves predictably, guaranteeing that logs are not unintentionally shared or corrupted across different calls.



Remaining Issues :

| Tool | Code | Issue Type | Line(s) | Description | Simple Fix to Get the Mark |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pylint** | `C0114` | Docstring | 1 | Missing module docstring. | Add `"""A system to manage inventory."""` at the top. |
| **Pylint** | `C0116` | Docstring | All `def`s | Missing function or method docstrings. | Add a docstring (`"""..."""`) inside every function. |
| **Pylint** | `C0103` | Naming | All `def`s | Function names are not `snake_case`. | Rename `addItem` to `add_item`, `loadData` to `load_data`, etc. (and update `main`). |
| **Pylint** | `C0209` | F-string | 14 | Using old `%` string formatting. | Change the log line to use an f-string: `logs.append(f"{datetime.now()}: Added {qty} of {item}")`. |
| **Pylint** | `R1732` | Design | 27, 35 | Not using a `with` statement for file operations. | Change `f = open(...)` and `f.close()` to use `with open(...)`. |
| **Pylint** | `W1514` | Design | 27, 35 | Not explicitly specifying file encoding. | Add `encoding="utf-8"` to `open()` calls. |
| **Pylint** | `W0603` | Global | 29 | Using the `global` statement is bad practice. | Refactor the code into an `InventorySystem` class (hardest fix, but best practice). |
| **Flake8** | `E302`/`E305` | Style | All `def`s | Need 2 blank lines between function definitions. | Add an extra blank line between every function. |
| **Bug** | N/A | Logic | 55 | **BUG:** `addItem(123, "ten")` will still cause a `TypeError` due to lack of validation. | Add an `if not isinstance(item, str) or not isinstance(qty, int): return` check to `addItem`. |