# Viva Questions and Answers (1-40)

All 40 questions from the class notebook, plus the extra **Q23.1**. Answers are grouped into eight files. Each answer has: concept, how it works, example, a ready interview answer, a "remember" list and a likely follow-up question.

**How to use:** read a file, then close it and answer each question out loud in your own words: *Definition -> How it works -> Example -> Practical importance.* Handwritten viva notes go in [`handwritten/`](handwritten/).

## Quick revision table

| # | Question (opens the answer) | One-line memory trigger |
|---|-----------------------------|-------------------------|
| 1 | [What is the difference between is and == in Python?](01_fundamentals_q01-05.md) | `==` compares values; `is` compares identity |
| 2 | [Difference between mutable and immutable objects/data structures, with examples.](01_fundamentals_q01-05.md) | Mutable can change; immutable cannot |
| 3 | [Difference between shallow copy and deep copy. Explain with a nested list example.](01_fundamentals_q01-05.md) | Shallow shares nested objects; deep copies them |
| 4 | [What are decorators in Python? Explain with their practical use.](01_fundamentals_q01-05.md) | Decorator adds behaviour without changing the original function |
| 5 | [What is a generator function? How are yield and return different?](01_fundamentals_q01-05.md) | `yield` pauses and produces values; `return` ends |
| 6 | [What is an iterator? Explain with an example.](02_iterators_and_oop_q06-10.md) | `iter()` and `next()`, keeps its position |
| 7 | [What is the difference between a class and an object? How do we create objects in Python?](02_iterators_and_oop_q06-10.md) | Class = blueprint; object = instance |
| 8 | [What is the difference between `__init__()` and `__new__()`?](02_iterators_and_oop_q06-10.md) | `__new__` creates; `__init__` initialises |
| 9 | [Explain inheritance and the different types of inheritance supported in Python.](02_iterators_and_oop_q06-10.md) | Child reuses parent; five types of inheritance |
| 10 | [What is the difference between method overloading and method overriding?](02_iterators_and_oop_q06-10.md) | Overloading = same name, different parameters; overriding = child redefines |
| 11 | [What is the difference between an error and an exception in Python?](03_exceptions_and_concurrency_q11-15.md) | Runtime problems that can be handled |
| 12 | [Explain try, except, and finally. What is their execution order?](03_exceptions_and_concurrency_q11-15.md) | try -> except -> finally (attempt, handle, clean up) |
| 13 | [How do we create custom exceptions in Python?](03_exceptions_and_concurrency_q11-15.md) | Inherit from `Exception`, use `raise` |
| 14 | [What is the Global Interpreter Lock (GIL) in Python?](03_exceptions_and_concurrency_q11-15.md) | One thread runs Python bytecode at a time in standard CPython |
| 15 | [What is the difference between multiprocessing and multithreading?](03_exceptions_and_concurrency_q11-15.md) | I/O-bound -> threads; CPU-bound -> processes |
| 16 | [What is the difference between NumPy arrays and traditional Python lists?](04_libraries_and_ai_code_review_q16-21.md) | NumPy: same type, vectorised; list: general-purpose |
| 17 | [What is Pandas? What is the difference between Series and DataFrame?](04_libraries_and_ai_code_review_q16-21.md) | Series = 1D; DataFrame = 2D |
| 18 | [What is Matplotlib? What types of visualizations can we create using it?](04_libraries_and_ai_code_review_q16-21.md) | Line = trend, bar = comparison, histogram = distribution, scatter = relationship |
| 19 | [If an AI generates a Python program, how would you review it to determine whether it is correct?](04_libraries_and_ai_code_review_q16-21.md) | Don't trust AI code: understand, test, check edge cases |
| 20 | [If an AI tool generates a program, what would you check before approving the code?](04_libraries_and_ai_code_review_q16-21.md) | Correctness, tests, edge cases, security, performance, maintainability |
| 21 | [Explain with an example how you would check code for security, performance, and maintainability.](04_libraries_and_ai_code_review_q16-21.md) | Review security, performance, maintainability (SQL injection example) |
| 22 | [How does Python manage memory? Explain reference counting and garbage collection.](05_memory_and_function_arguments_q22-25.md) | Reference counting + garbage collection (for cycles) |
| 23 | [What is the difference between break, continue, and pass in Python?](05_memory_and_function_arguments_q22-25.md) | `break` = stop, `continue` = skip, `pass` = do nothing |
| 23.1 | [What is the difference between del, remove(), and pop() in Python?](05_memory_and_function_arguments_q22-25.md) | `del` = index/slice, `remove()` = value, `pop()` = index and returns it |
| 24 | [What is the difference between local and global variables? Explain their scope.](05_memory_and_function_arguments_q22-25.md) | Local = inside function; global = outside (`global` keyword) |
| 25 | [What is the difference between `*args` and `**kwargs` in Python?](05_memory_and_function_arguments_q22-25.md) | `*args` = tuple; `**kwargs` = dictionary |
| 26 | [What are Python modules and packages? How does Python locate and import them?](06_modules_and_functional_q26-30.md) | Module = one file; package = directory of modules |
| 27 | [What is the difference between normal functions and lambda functions?](06_modules_and_functional_q26-30.md) | `def` vs `lambda` (one expression) |
| 28 | [What is recursion?](06_modules_and_functional_q26-30.md) | Function calls itself; needs a base case |
| 29 | [What is the difference between map(), filter(), and reduce()?](06_modules_and_functional_q26-30.md) | map = transform, filter = select, reduce = combine |
| 30 | [What is the difference between sort() and sorted() in Python?](06_modules_and_functional_q26-30.md) | `sort()` in place, returns None; `sorted()` returns a new list |
| 31 | [What are type hints in Python?](07_typing_mro_files_debugging_q31-35.md) | Optional annotations, not enforced at runtime |
| 32 | [What is Method Resolution Order (MRO) in Python?](07_typing_mro_files_debugging_q31-35.md) | Method search order (C3), `ClassName.mro()` |
| 33 | [What is the difference between read(), readline(), and readlines()?](07_typing_mro_files_debugging_q31-35.md) | `read()` = all, `readline()` = one line, `readlines()` = list |
| 34 | [What is the difference between text mode and binary mode when opening a file?](07_typing_mro_files_debugging_q31-35.md) | Text mode = `str`; binary mode = `bytes` |
| 35 | [How would you debug a Python program that runs without errors but produces incorrect output?](07_typing_mro_files_debugging_q31-35.md) | Logical error: expected vs actual, inspect, fix, retest |
| 36 | [What is the difference between synchronous and asynchronous programming?](08_async_frameworks_api_bigo_q36-40.md) | Sync = one after another; async = does not block while waiting |
| 37 | [What is the difference between async, def, and await in Python?](08_async_frameworks_api_bigo_q36-40.md) | `def`, `async def` (coroutine), `await` |
| 38 | [What are Django, Flask and FastAPI?](08_async_frameworks_api_bigo_q36-40.md) | Django full-featured, Flask lightweight, FastAPI modern APIs |
| 39 | [What is an API?](08_async_frameworks_api_bigo_q36-40.md) | APIs let apps talk; REST uses GET/POST/PUT/PATCH/DELETE |
| 40 | [What is Time Complexity? Why should a Python developer understand Big O notation when choosing data structures?](08_async_frameworks_api_bigo_q36-40.md) | Big O = growth rate; dict/set lookup O(1) average vs list O(n) |

## Files

| File | Questions |
|------|-----------|
| [01_fundamentals_q01-05.md](01_fundamentals_q01-05.md) | 1-5: `is` vs `==`, mutability, copying, decorators, generators |
| [02_iterators_and_oop_q06-10.md](02_iterators_and_oop_q06-10.md) | 6-10: iterators, classes, `__init__`/`__new__`, inheritance, overloading/overriding |
| [03_exceptions_and_concurrency_q11-15.md](03_exceptions_and_concurrency_q11-15.md) | 11-15: exceptions, try/except/finally, custom exceptions, GIL, threads vs processes |
| [04_libraries_and_ai_code_review_q16-21.md](04_libraries_and_ai_code_review_q16-21.md) | 16-21: NumPy, Pandas, Matplotlib, reviewing AI code |
| [05_memory_and_function_arguments_q22-25.md](05_memory_and_function_arguments_q22-25.md) | 22-25 and 23.1: memory management, break/continue/pass, del/remove/pop, scope, args/kwargs |
| [06_modules_and_functional_q26-30.md](06_modules_and_functional_q26-30.md) | 26-30: modules, lambda, recursion, map/filter/reduce, sort/sorted |
| [07_typing_mro_files_debugging_q31-35.md](07_typing_mro_files_debugging_q31-35.md) | 31-35: type hints, MRO, file reading, file modes, debugging |
| [08_async_frameworks_api_bigo_q36-40.md](08_async_frameworks_api_bigo_q36-40.md) | 36-40: sync vs async, async/await, web frameworks, APIs, Big O |
