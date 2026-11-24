# Viva answers: Questions 11-15: Exceptions and concurrency

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q11. What is the difference between an error and an exception in Python?

### Concept

An error is a problem that prevents a program from working correctly. An exception is an event that occurs during program execution and can often be handled using exception-handling mechanisms.

In practical Python discussions, errors such as ZeroDivisionError, TypeError, and ValueError are commonly handled as exceptions.

### How it works

Some problems occur while Python is executing the program, such as:

- Dividing by zero
- Accessing an invalid index
- Converting invalid input
- Opening a file that doesn't exist

We can use try and except to handle these situations instead of allowing the program to terminate unexpectedly.

### Example

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Output:**

```text
Cannot divide by zero
```

The exception is caught, allowing the program to continue.

### Interview answer

> "An error is a problem in a program that affects its execution, while an exception is a runtime event that can often be handled using Python's exception-handling mechanism. For example, dividing a number by zero raises a ZeroDivisionError. By using a try-except block, we can handle that exception gracefully instead of allowing the program to crash."

### Remember

- Error → Problem in program
- Exception → Runtime event that can be handled
- try → Risky code
- except → Handle problem
- Graceful handling

### Follow-up

**Q:** Can every error be handled using try-except?

**Hint:** Not every problem is recoverable. Syntax errors, for example, must generally be corrected before the program can execute.

## Q12. Explain try, except, and finally. What is their execution order?

### Concept

Python uses exception handling to manage runtime problems.

- try → Contains code that might raise an exception.
- except → Handles the exception.
- finally → Executes whether an exception occurs or not, typically for cleanup.

### How it works

The execution flow is:

1. Python executes the try block.
2. If an exception occurs, it looks for a matching except.
3. The matching handler executes.
4. The finally block executes afterward.

If no exception occurs, the except block is skipped, but finally still executes.

### Example

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program execution completed")
```

If the user enters 0, the ZeroDivisionError handler executes, followed by finally.

If the user enters "abc", the ValueError handler executes, followed by finally.

### Interview answer

> "The try block contains code that may raise an exception, the except block handles the exception, and the finally block executes regardless of whether an exception occurred. The finally block is commonly used for cleanup operations, such as closing files or releasing resources. For example, if a user enters zero while performing division, we can catch the ZeroDivisionError and display an appropriate message, while finally executes at the end."

### Remember

- try → Attempt
- except → Handle
- finally → Always executes in normal exception flow
- Cleanup operations
- Multiple except blocks are possible

### Follow-up

**Q:** Is finally guaranteed to execute in every possible situation?

**Hint:** Usually, but abrupt termination of the process or certain severe situations may prevent it from executing.

## Q13. How do we create custom exceptions in Python?

### Concept

A custom exception is an exception that we define ourselves to represent a specific problem in our application.

Python provides built-in exceptions, but sometimes application-specific situations need more meaningful exception names.

We create custom exceptions by inheriting from the Exception class.

### How it works

A custom exception helps us:

- Represent business-specific errors.
- Make error messages meaningful.
- Separate different failure conditions.
- Improve code readability and debugging.

### Example

```python
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    return balance - amount


try:
    withdraw(1000, 1500)

except InsufficientBalanceError as e:
    print(e)
```

**Output:**

```text
Insufficient balance
```

### Practical example

In a banking application, insufficient balance is a business-specific condition. Rather than using a generic exception, we create InsufficientBalanceError so that the application can handle it specifically.

### Interview answer

> "Custom exceptions are user-defined exceptions used to represent application-specific errors. We create them by inheriting from Python's Exception class and raise them using the raise keyword. For example, in a banking application, I can create an InsufficientBalanceError when a user tries to withdraw more money than their available balance. This makes error handling more meaningful and organized."

### Remember

- User-defined exception
- Inherit from Exception
- Use raise
- Business-specific errors
- Meaningful handling

### Follow-up

**Q:** Why would you create a custom exception instead of using a built-in exception?

**Hint:** To clearly represent a particular application or business condition and handle it separately.

## Q14. What is the Global Interpreter Lock (GIL) in Python?

### Concept

The Global Interpreter Lock (GIL) is a lock used by the standard CPython interpreter that allows only one thread at a time to execute Python bytecode within a process.

This means that even if we create multiple threads, they don't necessarily execute Python code simultaneously on multiple CPU cores.

### How it works

The GIL exists partly to simplify memory management and protect interpreter internals.

Its impact depends on the type of task:

- I/O-bound tasks: Multithreading can still be useful because threads can spend time waiting for I/O, allowing other threads to run.
- CPU-bound tasks: The GIL can limit the performance benefits of Python threads for CPU-intensive work.

### Example

Imagine four threads processing CPU-heavy calculations.

Even though there are four threads, in standard GIL-enabled CPython, only one thread executes Python bytecode at a time. Threads switch between execution, but this is not the same as four threads executing Python bytecode simultaneously on four cores.

For CPU-intensive work, multiprocessing may be more effective.

### Interview answer

> "The Global Interpreter Lock, or GIL, is a mechanism in the standard CPython interpreter that allows only one thread at a time to execute Python bytecode within a process. Because of this, multithreading may not provide true parallelism for CPU-bound Python code. However, threads are still useful for I/O-bound tasks such as network requests or file operations because they can work while other threads are waiting."

### Remember

- GIL → Global Interpreter Lock
- Standard CPython
- One thread executes Python bytecode at a time
- CPU-bound → Limited threading benefit
- I/O-bound → Multithreading can help

### Follow-up

**Q:** If Python has a GIL, why do we use multithreading?

**Hint:** Threads can overlap waiting periods for I/O operations, improving responsiveness and throughput.

## Q15. What is the difference between multiprocessing and multithreading?

### Concept

Both techniques allow us to perform multiple tasks concurrently, but they use different execution mechanisms.

- Multithreading: Multiple threads run within the same process and share memory.
- Multiprocessing: Multiple independent processes run, each with its own memory space.

### Comparison

| Feature | Multithreading | Multiprocessing |
|---|---|---|
| Unit | Threads | Processes |
| Memory | Shared | Separate |
| Resource usage | Generally lower | Generally higher |
| Communication | Easier through shared memory | Requires IPC mechanisms |
| GIL impact | Relevant in GIL-enabled CPython | Separate processes have separate GILs |
| Best suited for | I/O-bound tasks | CPU-bound tasks |

### How it works

Multithreading is useful when tasks spend time waiting, such as:

- Downloading files
- API requests
- Database queries
- Reading files

Multiprocessing is useful when tasks require significant CPU computation, such as:

- Image processing
- Large mathematical calculations
- Data processing
- Computational simulations

### Example

Suppose we need to download 10 files from the internet.

Using multithreading, several download operations can happen concurrently. While one thread waits for a network response, another can continue working.

But if we need to perform heavy mathematical calculations on 10 datasets, multiprocessing can distribute the work across CPU cores.

### Interview answer

> "Multithreading uses multiple threads within a single process, sharing the same memory, while multiprocessing uses multiple independent processes with separate memory spaces. Multithreading is generally useful for I/O-bound tasks such as API calls or file downloads, whereas multiprocessing is more suitable for CPU-bound tasks because it can utilize multiple CPU cores. For example, I would use multithreading to download multiple files concurrently and multiprocessing to perform computationally intensive data processing."

### Remember

- Thread → Shared process memory
- Process → Separate memory
- Multithreading → I/O-bound
- Multiprocessing → CPU-bound
- GIL → Important consideration for Python threads

### Follow-up

**Q:** What are the disadvantages of multiprocessing?

**Hint:** Higher memory consumption, process creation overhead, and more complex communication between processes.
