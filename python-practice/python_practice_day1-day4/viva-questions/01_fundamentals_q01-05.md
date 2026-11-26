# Viva answers: Questions 1-5: Python fundamentals

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q1. What is the difference between is and == in Python?

### Concept

Both operators compare things, but they compare different aspects:

- == checks whether two objects have the same value.
- is checks whether two variables refer to the same object in memory.

Think of two notebooks containing the same information. They may have identical contents, so == is true, but they are still two different notebooks, so is is false.

### How it works

```python
a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)  # True
print(a is b)  # False
```

Why?

- a == b → The lists contain the same elements.
- a is b → They are two separate list objects.

Now:

```python
a = [10, 20, 30]
b = a

print(a == b)  # True
print(a is b)  # True
```

Here, b = a does not create another list. Both variables refer to the same object.

### Example

Imagine two users have the same username:

```python
user1 = ["Nishant", 23]
user2 = ["Nishant", 23]

print(user1 == user2)  # True
print(user1 is user2)  # False
```

Their information is identical, but they are stored as separate objects.

### Interview answer

> "== checks whether two objects have equal values, whereas is checks whether both variables refer to the exact same object in memory. For example, two lists containing the same elements will return True with ==, but False with is if they are separate objects. I generally use == for value comparison and is when checking object identity, such as is None."

### Remember

- == → Value equality
- is → Object identity
- Same value ≠ same object
- Use is None for None checks

### Follow-up

**Q:** Why should we use is None instead of == None?

**Hint:** None is a singleton object. is None directly checks whether the object is that exact singleton.

## Q2. Difference between mutable and immutable objects/data structures, with examples.

### Concept

In Python, objects are classified based on whether their contents can be changed after creation.

- Mutable: Can be modified after creation.
- Immutable: Cannot be modified after creation.

This is important because it affects how variables behave, how objects are passed to functions, and how data is stored or shared.

### How it works

| Mutable | Immutable |
|---|---|
| Can change its contents | Cannot change its contents |
| list | tuple |
| dict | str |
| set | int |
| bytearray | float |

### Example

Mutable example:

```python
numbers = [10, 20, 30]
numbers[0] = 100

print(numbers)
# [100, 20, 30]
```

The existing list was modified.

Immutable example:

```python
name = "Python"
name[0] = "J"  # TypeError
```

Strings are immutable. To create a modified string, we need to create a new string:

```python
name = "Python"
name = "J" + name[1:]

print(name)
# Jython
```

The original string wasn't modified. A new string was created and the variable was reassigned.

### Practical example

Imagine a shopping cart:

```python
cart = ["Laptop", "Mouse"]
cart.append("Keyboard")
```

A shopping cart is naturally represented by a mutable list because items may be added or removed.

But a fixed product ID could be represented using an immutable integer or string.

### Interview answer

> "Mutable objects can be modified after they are created, whereas immutable objects cannot be changed after creation. Lists, dictionaries and sets are examples of mutable objects, while strings, integers and tuples are immutable. For example, I can modify an element of a list directly, but modifying a character in a string raises an error. Mutable objects are useful when data needs to change, while immutability helps maintain predictable values."

### Remember

- Mutable → Changeable
- Immutable → Cannot be changed
- List, dictionary, set → Mutable
- String, tuple, integer → Immutable
- Modification vs creation of a new object

### Follow-up

**Q:** Is a tuple always completely immutable?

**Hint:** The tuple itself cannot be modified, but if it contains a mutable object such as a list, that inner list may still be modified.

Example:

```python
t = (10, [20, 30])
```

t[1].append(40)

```python
print(t)
# (10, [20, 30, 40])
```

This is a subtle but excellent viva point!

## Q3. Difference between shallow copy and deep copy. Explain with a nested list example.

### Concept

When copying a collection, we need to understand whether the objects inside it are also copied.

- Shallow copy: Creates a new outer object, but references the same nested objects.
- Deep copy: Creates a new outer object and recursively copies the nested objects as well.

Imagine copying a folder containing other folders.

- Shallow copy: You copy the main folder structure, but both copies point to the same inner folders.
- Deep copy: You duplicate the inner folders too.

### How it works

Let's use a nested list:

```python
original = [[1, 2], [3, 4]]
```

A shallow copy creates a new outer list but shares the inner lists.

A deep copy creates independent nested lists.

### Example

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 100

print(original)
print(shallow)
print(deep)
```

**Output:**

```text
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
[[1, 2], [3, 4]]
```

Why?

- shallow shares the inner list with original.
- deep has its own independent nested objects.

### Visual understanding

```text
Shallow copy: new outer list, SAME inner lists

original  ->  [ A , B ]
                 | |
shallow   ->  [ A , B ]      (A and B are shared)

Deep copy: new outer list, NEW inner lists

original  ->  [ A  , B  ]
deep      ->  [ A' , B' ]    (A' and B' are independent copies)
```

### Interview answer

> "A shallow copy creates a new outer object, but its nested objects are still shared with the original. A deep copy recursively creates copies of the nested objects as well. For example, if I shallow-copy a nested list and modify an inner list, the change will also appear in the original. But with copy.deepcopy(), the nested structures are independent, so changes in one don't affect the other."

### Remember

- copy.copy() → Shallow copy
- copy.deepcopy() → Deep copy
- Shallow → Outer object copied, inner references shared
- Deep → Nested objects copied recursively
- Nested structures are the key difference

### Follow-up

**Q:** What happens if you shallow-copy a simple list of integers?

**Hint:** Since integers are immutable, modifying the list's elements generally won't create the same shared-mutation problem seen with nested mutable objects.

## Q4. What are decorators in Python? Explain with their practical use.

### Concept

A decorator is a function that modifies or extends the behavior of another function without changing its original code.

Think of it like adding a feature to an existing application without rewriting the application itself.

For example, you might want to add:

- Logging
- Authentication
- Timing
- Validation
- Caching

Instead of adding this code to every function, you can use a decorator.

### How it works

A decorator generally:

1. Takes a function as input.
2. Defines a wrapper function.
3. Adds extra behavior before or after the original function.
4. Calls the original function.
5. Returns the wrapper.

The @decorator_name syntax is a convenient way to apply a decorator.

### Example

Let's create a decorator that measures how long a function takes.

```python
import time

def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print("Execution time:", end - start)

    return wrapper


@timer
def task():
    print("Task is running")


task()
```

The decorator adds timing functionality to task() without modifying the function itself.

### Practical example

In a web application, we might want to log every function call.

Instead of writing logging code repeatedly:

```python
def login():
    print("Function called")
    # login logic

def register():
    print("Function called")
    # registration logic
```

We can create one logging decorator and reuse it for many functions.

### Interview answer

> "A decorator in Python is a function that adds or modifies the behavior of another function without changing its original implementation. It works by taking the original function, wrapping it with another function, and returning that wrapper. Decorators are commonly used for logging, authentication, timing and caching. For example, I can create a timing decorator that measures how long a function takes to execute and apply it to multiple functions using the @ syntax."

### Remember

- Decorator → Modify behavior
- Doesn't require modifying original function
- Wrapper function
- @ syntax
- Logging, timing, authentication, caching

### Follow-up

**Q:** What is the purpose of `*args` and `**kwargs` in a decorator?

**Hint:** They allow the wrapper to support functions with different numbers and types of arguments.

A more reusable decorator would use:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

## Q5. What is a generator function? How are yield and return different?

### Concept

A generator function is a function that produces values one at a time instead of generating and returning all values at once.

It uses the yield keyword.

The most important difference:

- return → Ends the function and returns a result.
- yield → Produces a value and temporarily pauses the function, preserving its state.

When the generator is requested again, execution continues from where it paused.

### How it works

A normal function:

```python
def numbers():
    return [1, 2, 3, 4, 5]
```

This creates and returns the entire list.

A generator function:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

It produces the values one by one when requested.

Generators are useful when:

- Working with large datasets.
- Processing files.
- Streaming data.
- Saving memory.
- Producing values gradually.

### Example

```python
def count():
    yield 1
    yield 2
    yield 3

gen = count()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

Each call to next() retrieves the next value.

After the final value, another next() raises StopIteration.

### Practical example

Imagine reading a very large file containing 1 million lines.

Instead of loading every line into memory:

```python
def read_lines(file):
    for line in file:
        yield line
```

The generator allows us to process one line at a time, which can significantly reduce memory usage.

### Interview answer

> "A generator function is a function that uses yield to produce values one at a time. Unlike return, which terminates the function, yield pauses execution and preserves the function's state. When the next value is requested, execution resumes from that point. Generators are useful for processing large datasets or files because they don't need to store all the values in memory at once. For example, I can use a generator to read a large file line by line."

### Remember

- yield → Produce and pause
- return → Finish function
- State is preserved
- Values produced lazily
- Memory-efficient processing

### Follow-up

**Q:** What is lazy evaluation?

**Hint:** Values are produced only when requested, rather than being generated immediately in advance.
