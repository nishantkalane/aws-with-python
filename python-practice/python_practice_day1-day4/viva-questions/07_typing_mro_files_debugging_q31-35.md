# Viva answers: Questions 31-35: Type hints, MRO, file handling and debugging

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q31. What are type hints in Python?

### Concept

Type hints are optional annotations that indicate the expected data types of variables, function parameters and return values.

Python is dynamically typed, meaning we don't have to declare variable types explicitly. However, type hints make code easier to understand and maintain.

### How it works

Without type hints:

```python
def add(a, b):
    return a + b
```

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

- a: int means a is expected to be an integer.
- b: int means b is expected to be an integer.
- -> int means the function is expected to return an integer.

**Important:** Python generally does not enforce type hints at runtime. Tools such as MyPy and Pyright can check them statically.

### Example

Consider a function that calculates an employee's salary after a bonus.

```python
def calculate_salary(
    salary: float,
    bonus: float
) -> float:

    return salary + bonus


print(calculate_salary(30000.0, 5000.0))
```

**Output:**

```text
35000.0
```

The type hints tell another developer what kind of values the function expects.

### Interview answer

> "Type hints in Python are optional annotations that specify the expected data types of variables, function parameters and return values. They improve code readability, documentation and maintainability. For example, I can specify that a salary calculation function accepts two float values and returns a float. Python doesn't generally enforce these annotations at runtime, but tools like MyPy and Pyright can use them for static type checking."

### Remember

- Optional annotations
- variable: type
- -> return_type
- Readability and maintainability
- MyPy and Pyright

### Follow-up

**Q:** Are type hints compulsory in Python?

No. They are optional and Python generally doesn't enforce them at runtime.

## Q32. What is Method Resolution Order (MRO) in Python?

### Concept

Method Resolution Order (MRO) is the order in which Python searches for a method or attribute when a class inherits from multiple classes.

It becomes particularly important in multiple inheritance, where multiple parent classes may contain methods with the same name.

### How it works

Python uses an algorithm called C3 linearization to determine the method resolution order.

Let's understand with an example:

```python
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


obj = D()
obj.show()
```

**Output:**

```text
Class B
```

Why?

Because Python searches according to the MRO:

D → B → C → A → object

Since B comes before C in the inheritance declaration, Python finds show() in B first.

We can check MRO using:

```python
print(D.mro())
```

### Example

Imagine a software application where multiple parent classes provide the same functionality.

For example:

- Logger provides a logging method.
- Database provides a logging method.
- Application inherits from both.

MRO determines which implementation Python uses when the child class calls that method.

### Interview answer

> "Method Resolution Order, or MRO, defines the order in which Python searches for methods and attributes in an inheritance hierarchy. It is especially important in multiple inheritance when different parent classes contain methods with the same name. Python uses C3 linearization to determine this order. For example, if a class inherits from B and C, and both inherit from A, Python follows a consistent resolution order. We can inspect it using the mro() method."

### Remember

- MRO → Method search order
- Multiple inheritance
- C3 linearization
- ClassName.mro()
- super() follows MRO

### Follow-up

**Q:** What is the purpose of super() in Python?

super() provides access to methods in the next class in the MRO, commonly used to call parent or cooperative superclass methods.

## Q33. What is the difference between read(), readline(), and readlines()?

### Concept

All three are file-reading methods in Python, but they differ in how much data they read.

- read() → Reads the entire file or a specified number of characters/bytes.
- readline() → Reads one line at a time.
- readlines() → Reads all remaining lines and returns them as a list.

### How it works

Suppose a file contains:

```text
Python
Java
C++
```

| Method | What it returns |
|---|---|
| read() | Entire content as a string |
| readline() | One line as a string |
| readlines() | List of lines |

### Example

Assume data.txt contains:

```text
Python
Java
C++
```

#### A. read()

```python
with open("data.txt", "r") as file:
    print(file.read())
```

**Output:**

```text
Python
Java
C++
```

#### B. readline()

```python
with open("data.txt", "r") as file:
    print(file.readline())
```

**Output:**

```text
Python
```

#### C. readlines()

```python
with open("data.txt", "r") as file:
    print(file.readlines())
```

**Output:**

```text
['Python\n', 'Java\n', 'C++']
```

Notice that newline characters are preserved where present.

### Interview answer

> "The main difference between read, readline and readlines is how they retrieve file content. Read retrieves the entire remaining file content as a string, readline reads one line at a time, and readlines reads all remaining lines and returns them as a list. For example, if I have a file containing thousands of records, readline can help me process it line by line instead of loading everything into memory."

### Remember

- read() → Entire content
- readline() → One line
- readlines() → List of lines
- Newline characters may be preserved
- Line-by-line processing is useful for large files

### Follow-up

**Q:** Which method would you prefer for reading a very large file?

A line-by-line iteration is generally preferable because it avoids loading the entire file into memory.

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line)
```

## Q34. What is the difference between text mode and binary mode when opening a file?

### Concept

Python supports two main modes for reading and writing files:

- Text mode (t): Reads and writes data as text (strings).
- Binary mode (b): Reads and writes raw bytes.

The main difference is the type of data handled by the file.

### How it works

| Text Mode | Binary Mode |
|---|---|
| Handles strings (str) | Handles bytes (bytes) |
| Performs character encoding and decoding | No automatic text decoding or encoding |
| Suitable for text files | Suitable for images, audio, videos and other binary files |
| Default mode when opening a file | Must be specified explicitly |

Common file modes:

- "r" → Read text
- "w" → Write text
- "rb" → Read binary
- "wb" → Write binary

### Example

#### A. Text mode

```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

Reading it:

```python
with open("data.txt", "r") as file:
    data = file.read()

print(data)
print(type(data))
```

**Output:**

```text
Hello Python
<class 'str'>
```

#### B. Binary mode

```python
with open("image.jpg", "rb") as file:
    data = file.read()

print(type(data))
```

**Output:**

```text
<class 'bytes'>
```

Here, Python reads the image as raw bytes rather than attempting to interpret it as text.

### Interview answer

> "Python provides text and binary modes for file handling. Text mode works with strings and performs encoding and decoding, whereas binary mode works directly with bytes without automatic text decoding. Text mode is suitable for files such as TXT and CSV, while binary mode is used for images, audio and videos. For example, I would open a text file using r mode and an image using rb mode."

### Remember

- Text → str
- Binary → bytes
- "r" → Read text
- "rb" → Read binary
- Text mode handles encoding and decoding

### Follow-up

**Q:** Why should we use binary mode when copying an image?

Because binary mode preserves the original bytes without interpreting or modifying them as text.

## Q35. How would you debug a Python program that runs without errors but produces incorrect output?

### Concept

This situation is called a logical error.

The program executes successfully without syntax errors or runtime exceptions, but the output is incorrect because the implemented logic is wrong.

For example, a program may calculate an average incorrectly because it divides by the wrong number.

### How it works

I would follow a systematic debugging approach:

1. Understand the expected output: Identify what the program should produce.
2. Reproduce the issue: Run the program using the same input.
3. Check intermediate values: Use print() or a debugger to inspect variables.
4. Trace the execution: Identify where the actual result starts differing from the expected result.
5. Fix the logic: Correct the faulty condition or calculation.
6. Retest: Test normal inputs and edge cases.

Useful debugging tools include:

- print() statements
- Python's built-in pdb debugger
- Breakpoints in VS Code or PyCharm
- Unit tests using pytest

### Example

Suppose AI generates this function to calculate the average of numbers:

```python
def average(numbers):
    total = sum(numbers)

    return total / (len(numbers) - 1)


print(average([10, 20, 30]))
```

**Output:**

```text
30.0
```

But the expected answer is:

`(10+20+30)/3=20`

The program doesn't produce an error, but the denominator is incorrect.

Correct implementation:

```python
def average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)

    return total / len(numbers)


print(average([10, 20, 30]))
```

**Output:**

```text
20.0
```

The issue was in the calculation logic, not Python syntax.

### Interview answer

> "If a Python program runs without errors but produces incorrect output, I would suspect a logical error. First, I would understand the expected output and reproduce the problem using the same input. Then I would inspect intermediate variable values using print statements or debugging tools like pdb or PyCharm breakpoints. I would identify where the actual result differs from the expected result, correct the logic and test it again with normal and edge cases. For example, if an average calculation uses the wrong denominator, the program may execute successfully but return an incorrect result."

### Remember

- Logical error
- Expected vs actual output
- Reproduce the issue
- Inspect intermediate values
- Fix and retest

### Follow-up

**Q:** What is the difference between a syntax error, runtime error and logical error?

| Error | Meaning | Example |
|---|---|---|
| Syntax | Invalid Python syntax | Missing colon |
| Runtime | Error during execution | Division by zero |
| Logical | Program executes but gives incorrect output | Wrong formula |
