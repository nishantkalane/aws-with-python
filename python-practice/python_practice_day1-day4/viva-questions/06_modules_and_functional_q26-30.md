# Viva answers: Questions 26-30: Modules and functional programming

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q26. What are Python modules and packages? How does Python locate and import them?

### Concept

Python provides modules and packages to organize code into reusable and manageable components.

- Module: A single Python file (.py) containing functions, classes or variables.
- Package: A directory that organizes related Python modules together.

Think of a module as one chapter of a book and a package as the complete book containing multiple chapters.

### How it works

Suppose we have a project with several mathematical operations.

Instead of writing everything in one file, we can organize it like this:

```text
my_project/
├── main.py
└── math_operations/
    ├── __init__.py
    ├── add.py
    ├── subtract.py
    └── multiply.py
```

How do we import a module?

Suppose add.py contains:

```python
def add(a, b):
    return a + b
```

Inside main.py:

```python
from math_operations.add import add

print(add(10, 20))
```

**Output:**

```text
30
```

How does Python locate a module?

Python searches for modules using its import system, which includes:

1. Already loaded modules in sys.modules.
2. Built-in and registered import finders.
3. Locations in sys.path, including the script directory and configured import paths.

The exact search process also depends on the import configuration.

You can inspect the search paths using:

```python
import sys

print(sys.path)
```

### Example

In your data analysis projects, you might create:

- cleaning.py for data cleaning.
- visualization.py for charts.
- analysis.py for calculations.

You can import functions from these files into your main program rather than repeating the same code.

### Interview answer

> "A module is a single Python file containing reusable functions, classes or variables, whereas a package is a collection of related modules organized into a directory. We use them to organize code and improve reusability. For example, I can create separate modules for data cleaning and visualization and import them into my main application. Python locates modules through its import system, using locations such as the script directory and paths available in sys.path."

### Remember

- Module → Single .py file
- Package → Collection of modules
- import → Import module
- from ... import ... → Import specific objects
- sys.path → Module search paths

### Follow-up

**Q:** What is the purpose of `__init__.py`?

It can mark a directory as a regular Python package and can contain package initialization code. Modern Python also supports namespace packages without it.

## Q27. What is the difference between normal functions and lambda functions?

### Concept

Both normal functions and lambda functions are used to perform operations, but they differ in how they are defined.

- Normal function: Defined using the def keyword and can contain multiple statements.
- Lambda function: A small anonymous function defined using the lambda keyword, containing a single expression.

### How it works

| Normal Function | Lambda Function |
|---|---|
| Uses def | Uses lambda |
| Has a function name | Anonymous by default |
| Can contain multiple statements | Contains one expression |
| Can use explicit return | Expression result is returned automatically |
| Suitable for complex logic | Suitable for short operations |

### Example

Normal function:

```python
def square(n):
    return n * n

print(square(5))
```

**Output:**

```text
25
```

Lambda function:

```python
square = lambda n: n * n

print(square(5))
```

**Output:**

```text
25
```

Both perform the same operation.

### Practical example

Suppose we have a list of students and want to sort them according to their marks.

```python
students = [
    ("Nishant", 85),
    ("Rahul", 90),
    ("Aman", 78)
]

students.sort(key=lambda x: x[1])

print(students)
```

**Output:**

```text
[('Aman', 78), ('Nishant', 85), ('Rahul', 90)]
```

Here, the lambda function extracts the marks from each tuple for sorting.

### Interview answer

> "A normal function is defined using the def keyword and can contain multiple statements, whereas a lambda function is a small anonymous function defined using the lambda keyword and contains a single expression. Both can perform similar operations. For example, I can use a lambda function to square a number or provide a sorting key when sorting student records based on marks. Lambda functions are particularly useful for short operations."

### Remember

- Normal → def
- Lambda → lambda
- Normal function → Multiple statements
- Lambda → Single expression
- Common use → map(), filter(), sorting

### Follow-up

**Q:** Can a lambda function have multiple arguments?

Yes!

```python
add = lambda a, b: a + b

print(add(10, 20))
```

**Output:**

```text
30
```

It can accept multiple arguments but contains only one expression.

## Q28. What is recursion?

### Concept

Recursion is a programming technique in which a function calls itself to solve a problem.

Instead of solving the entire problem at once, we break it into smaller versions of the same problem.

Every properly designed recursive function needs two important components:

1. Base case: The condition that stops recursion.
2. Recursive case: The part where the function calls itself with a smaller or simpler problem.

### How it works

Let's understand factorial.

Factorial of 5:

`5! = 5 × 4 × 3 × 2 × 1`

We can represent it recursively:

`n! = n × (n-1)!`

Base case:

`0! = 1`

### Example

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

**Output:**

```text
120
```

### Dry run

```text
factorial(5)
 = 5 * factorial(4)
 = 5 * (4 * factorial(3))
 = 5 * (4 * (3 * factorial(2)))
 = 5 * (4 * (3 * (2 * factorial(1))))
 = 5 * (4 * (3 * (2 * (1 * factorial(0)))))
factorial(0) returns 1   <- base case, recursion stops

Values come back in reverse order:
1 -> 1*1 = 1 -> 2*1 = 2 -> 3*2 = 6 -> 4*6 = 24 -> 5*24 = 120
```

### Interview answer

> "Recursion is a technique where a function calls itself to solve a problem by breaking it into smaller subproblems. Every recursive function needs a base case to stop the recursion and a recursive case to continue the process. For example, factorial can be calculated recursively by multiplying a number with the factorial of the previous number. Recursion is commonly used in tree traversal, searching and divide-and-conquer algorithms."

### Remember

- Function calls itself
- Base case → Stops recursion
- Recursive case → Smaller problem
- Call stack
- Factorial, tree traversal, divide and conquer

### Follow-up

**Q:** What happens if we forget the base case?

The function may continue calling itself until Python raises a RecursionError, typically because the recursion depth limit is exceeded.

## Q29. What is the difference between map(), filter(), and reduce()?

### Concept

These are Python functions used for processing collections of data.

- map() → Applies a function to every element.
- filter() → Selects elements that satisfy a condition.
- reduce() → Combines elements into a single result by repeatedly applying a function.

The easiest way to remember them:

Map = Transform, Filter = Select, Reduce = Combine.

### How it works

| Function | Purpose | Result |
|---|---|---|
| map() | Transform each element | Iterator |
| filter() | Select matching elements | Iterator |
| reduce() | Combine elements | Single accumulated value |

Note: reduce() is available through the functools module.

### Example

Let's use:

```python
numbers = [1, 2, 3, 4, 5]
```

#### A. map()

Suppose we want to square every number.

```python
result = map(lambda x: x*x, numbers)

print(list(result))
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

Every element is transformed.

#### B. filter()

Suppose we want only even numbers.

```python
result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

**Output:**

```text
[2, 4]
```

Only elements satisfying the condition are selected.

#### C. reduce()

Suppose we want the sum of all numbers.

```python
from functools import reduce

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

**Output:**

```text
15
```

Let's understand the reduction:

- 1 + 2 = 3
- 3 + 3 = 6
- 6 + 4 = 10
- 10 + 5 = 15

### Interview answer

> "map, filter and reduce are functions used for processing collections. Map applies a function to every element, filter selects elements based on a condition, and reduce combines all elements into a single result. For example, with a list of numbers, I can use map to square every number, filter to select even numbers, and reduce to calculate their sum. Reduce is imported from the functools module."

### Remember

- Map → Transform
- Filter → Select
- Reduce → Combine
- map() and filter() → Iterators
- reduce() → functools

### Follow-up

**Q:** What is the difference between map and filter?

Map changes or transforms each element, whereas filter selects only the elements satisfying a condition.

## Q30. What is the difference between sort() and sorted() in Python?

### Concept

Both are used to arrange elements in ascending or descending order.

However, their main difference is whether they modify the original collection.

- sort() → Modifies the original list.
- sorted() → Returns a new sorted list without modifying the original iterable.

### How it works

| Feature | sort() | sorted() |
|---|---|---|
| Type | List method | Built-in function |
| Original list | Modified | Unchanged |
| Returns | None | New sorted list |
| Works with | Lists | Any iterable |
| Reverse sorting | reverse=True | reverse=True |

Both support the key argument for custom sorting.

### Example

#### A. Using sort()

```python
numbers = [5, 2, 8, 1]

result = numbers.sort()

print(numbers)
print(result)
```

**Output:**

```text
[1, 2, 5, 8]
None
```

The original list is modified, and sort() returns None.

#### B. Using sorted()

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers)

print(numbers)
print(result)
```

**Output:**

```text
[5, 2, 8, 1]
[1, 2, 5, 8]
```

The original list remains unchanged.

### Practical example

Suppose you have student marks and want to display them in sorted order without changing the original records.

You can use:

```python
marks = [85, 70, 95, 60]

sorted_marks = sorted(marks)

print(sorted_marks)
print(marks)
```

This preserves the original list.

### Interview answer

> "sort() and sorted() both arrange elements in order, but they differ in how they handle the original data. The sort method works directly on a list and modifies it in place, returning None. The sorted function works with any iterable and returns a new sorted list without changing the original collection. For example, if I want to sort student marks while preserving the original list, I would use sorted()."

### Remember

- sort() → In-place
- sorted() → New list
- sort() → Returns None
- sorted() → Returns sorted list
- Both support reverse=True and key=

### Follow-up

**Q:** How do you sort a list in descending order?

```python
numbers = [5, 2, 8, 1]

numbers.sort(reverse=True)

print(numbers)
```

**Output:**

```text
[8, 5, 2, 1]
```
