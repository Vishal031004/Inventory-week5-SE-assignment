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
Easiest: The easiest ones were eval() and the unused logging import. They were super simple fixes. I just had to delete the line or replace eval() with print(). Didn't have to think much, just do what the tool said.

Hardest: The hardest one was definitely that logs=[] bug (the "mutable default argument"). It's not a crash, it's a weird logic bug, so it's way harder to spot. I had to actually understand why using a list there was bad, and then remember the None trick to fix it. That took more brainpower than just fixing a typo.

2. Did the static analysis tools report any false positives? If so, describe one example.
Honestly, no. For this lab, the tools were pretty spot on. All the big issues they found, like the eval() call, the bare except:, and that logs=[] bug, were 100% real problems.

The only things that felt like "false positives" were all the Pylint style warnings (like C0103 for function names not being snake_case). It's not really a bug, just a style choice, so a team might decide to ignore those. But all the major warnings were legit.

3. How would you integrate static analysis tools into your actual software development workflow?
I'd use them in two main places:

1. On my own laptop: I'd set up a pre-commit hook. That's a git thing that can automatically run a fast tool like Flake8 before it even lets me make a commit. It's awesome for catching all my messy formatting and style errors before they even get into the project.

2. For the whole team (in CI/CD): I'd use GitHub Actions. Every time someone makes a pull request, a server would automatically run the full set of tools—Pylint for deep checks, Bandit for security. If any tool finds a big error, the build fails. This blocks anyone from merging bad code until they fix it.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
The code got way better, for real.

It's more robust: It won't crash as easily. Changing except: to except KeyError: means the code now knows exactly what error to expect (a missing item) and won't accidentally hide other system-level crashes.

It's way safer: Getting rid of that eval() call (thanks, Bandit!) patched a huge security hole.

It actually works right: Fixing the logs=[] bug means the addItem function will stop acting weird by sharing logs between calls. The code is just cleaner and easier to trust now.