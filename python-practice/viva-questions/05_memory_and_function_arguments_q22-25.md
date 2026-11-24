# Viva answers: Questions 22-25 (and 23.1): Memory, control flow and function arguments

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q22. How does Python manage memory? Explain reference counting and garbage collection.

### Concept

Python manages memory automatically. As developers, we generally don't need to manually allocate and release memory.

Python handles:

- Allocating memory when objects are created.
- Keeping track of objects that are being used.
- Releasing memory when objects are no longer needed.

Two important concepts are reference counting and garbage collection.

### How it works

#### A. Reference Counting

Python keeps track of how many references point to an object.

When an object is no longer referenced, its reference count can become zero, and its memory can be reclaimed.

Example:

```python
a = [10, 20, 30]
b = a
```

Here, both a and b refer to the same list.

```python
del a
```

Now b still refers to the list, so the object is not destroyed.

When we execute:

```python
del b
```

There are no remaining references from these variables, so the object's reference count can reach zero.

#### B. Garbage Collection

Reference counting alone cannot handle every situation.

For example, two objects may refer to each other even though nothing outside the pair uses them. This is called a reference cycle.

Python's cyclic garbage collector detects and reclaims unreachable reference cycles.

### Example

```python
import gc

class Student:
    pass

a = Student()
b = Student()

a.friend = b
b.friend = a

del a
del b

print(gc.collect())
```

Here, both objects refer to each other. Even after deleting the variables, the objects can form an unreachable reference cycle.

The garbage collector can detect and reclaim such cycles.

### Interview answer

> "Python manages memory automatically, so we generally don't need to allocate or release memory manually. One important mechanism is reference counting, where Python tracks how many references point to an object. When the reference count becomes zero, the object's memory can be reclaimed. Python also uses a garbage collector to identify unreachable reference cycles, where objects refer to each other but are no longer accessible. This helps manage memory efficiently without requiring manual memory management."

### Remember

- Automatic memory management
- Reference counting
- Reference count reaches zero
- Circular references
- Garbage collection

### Follow-up

**Q:** Why is garbage collection needed if Python already uses reference counting?

Because reference counting alone cannot reclaim unreachable objects that form reference cycles.

## Q23. What is the difference between break, continue, and pass in Python?

### Concept

All three are Python control-flow statements, but they have different purposes.

- break → Completely terminates the loop.
- continue → Skips the current iteration and moves to the next iteration.
- pass → Does nothing. It acts as a placeholder.

### How it works

Consider a loop that runs from 1 to 5.

| Statement | What happens |
|---|---|
| break | Stops the entire loop |
| continue | Skips one iteration |
| pass | Does nothing and continues normally |

### Example

#### A. break

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

**Output:**

```text
1
2
```

When i becomes 3, the entire loop terminates.

#### B. continue

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

**Output:**

```text
1
2
4
5
```

When i becomes 3, only that iteration is skipped.

#### C. pass

```python
for i in range(1, 6):
    if i == 3:
        pass

    print(i)
```

**Output:**

```text
1
2
3
4
5
```

pass doesn't change the flow of execution.

### Interview answer

> "Break, continue and pass are control-flow statements in Python. Break terminates the entire loop, continue skips the current iteration and moves to the next one, while pass does nothing and acts as a placeholder. For example, if I'm searching for a particular element, I can use break once I find it. I can use continue to skip unwanted values, and pass when I want to define a block without implementing it yet."

### Remember

- break → Stop loop
- continue → Skip iteration
- pass → Do nothing
- Break exits completely.
- Continue keeps the loop running.

### Follow-up

**Q:** Can we use break outside a loop?

No. Using break outside a loop raises a SyntaxError.

## Q23.1. What is the difference between del, remove(), and pop() in Python? (extra question)

### Concept

All three can be used to remove elements from a list, but they differ in how they identify and remove elements.

- del → Deletes an element or a range using its index or deletes a variable binding.
- remove() → Removes the first occurrence of a specified value.
- pop() → Removes an element using its index and returns the removed element.

### How it works

| Feature | del | remove() | pop() |
|---|---|---|---|
| Works using | Index/slice | Value | Index |
| Returns removed element | No | No | Yes |
| Removes first matching value | No | Yes | No |
| Default index | Not applicable | Not applicable | Last element |

### Example

Let's consider:

```python
numbers = [10, 20, 30, 40, 20]
```

#### A. Using del

```python
del numbers[1]

print(numbers)
```

**Output:**

```text
[10, 30, 40, 20]
```

It deletes the element at index 1.

#### B. Using remove()

```python
numbers = [10, 20, 30, 40, 20]

numbers.remove(20)

print(numbers)
```

**Output:**

```text
[10, 30, 40, 20]
```

It removes the first occurrence of value 20.

#### C. Using pop()

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print(removed)
print(numbers)
```

**Output:**

```text
20
[10, 30, 40]
```

It removes and returns the element at index 1.

### Interview answer

> "The main difference between del, remove and pop is how they identify the element and whether they return it. Del deletes an element using its index or a slice, remove deletes the first occurrence of a specified value, and pop removes an element by index and returns that element. For example, if I want to remove the value 20, I use remove(20), but if I want to remove the element at index 1 and retrieve it, I use pop(1)."

### Remember

- del → Index or slice
- remove() → Value
- pop() → Index + returns element
- remove() removes first occurrence
- pop() without an index removes the last element

### Follow-up

**Q:** What happens if the specified value is not present when using remove()?

It raises a ValueError.

## Q24. What is the difference between local and global variables? Explain their scope.

### Concept

A variable's scope determines where that variable can be accessed in a program.

There are two common types:

- Local variable: Created inside a function and normally accessible only within that function.
- Global variable: Defined outside functions and accessible throughout the module, subject to Python's scope rules.

### How it works

Consider this:

```python
x = 100  # Global variable

def display():
    y = 50  # Local variable

    print(x)
    print(y)

display()
```

**Output:**

```text
100
50
```

The function can access the global variable x and its own local variable y.

However, y cannot normally be accessed outside the function.

What if we want to modify a global variable inside a function?

We use the global keyword.

### Example

```python
count = 10

def update():
    global count
    count = 20

update()

print(count)
```

**Output:**

```text
20
```

Without global, assigning to count inside the function would create a local variable instead.

### Interview answer

> "A local variable is declared inside a function and is generally accessible only within that function, whereas a global variable is declared outside functions and can be accessed throughout the module. If I want to modify a global variable inside a function, I use the global keyword. For example, if I define a counter outside a function and want to update its value inside the function, I can use global to modify the original variable."

### Remember

- Local → Inside function
- Global → Outside function
- Scope → Where variable is accessible
- global → Modify global binding
- Local variables are not normally accessible outside their function

### Follow-up

**Q:** What happens if a local and global variable have the same name?

The local variable takes precedence inside that function when the name is bound locally.

Example:

```python
x = 100

def show():
    x = 50
    print(x)

show()
print(x)
```

**Output:**

```text
50
100
```

## Q25. What is the difference between `*args` and `**kwargs` in Python?

### Concept

Both `*args` and `**kwargs` allow us to pass a variable number of arguments to a function.

- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dictionary.

They make functions more flexible.

### How it works

#### A. `*args`

Suppose we don't know how many numbers the user will pass.

```python
def add(*args):
    print(args)
    return sum(args)

print(add(10, 20, 30))
```

**Output:**

```text
(10, 20, 30)
60
```

All positional arguments are collected into a tuple.

#### B. `**kwargs`

Suppose we don't know how many named details the user will provide.

```python
def student(**kwargs):
    print(kwargs)

student(name="Nishant", age=23, city="Nagpur")
```

**Output:**

```text
{'name': 'Nishant', 'age': 23, 'city': 'Nagpur'}
```

All keyword arguments are collected into a dictionary.

### Practical example

Imagine creating a function for student registration.

Some students may provide only their name and age, while others may also provide their city, college or email.

```python
def register(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key, ":", value)


register("Nishant", age=23, city="Nagpur")
```

**Output:**

```text
Name: Nishant
age : 23
city : Nagpur
```

### Interview answer

> "`*args` and `**kwargs` are used when we want a function to accept a variable number of arguments. `*args` collects positional arguments into a tuple, whereas `**kwargs` collects keyword arguments into a dictionary. For example, I can use `*args` to create a function that adds any number of numbers, and `**kwargs` to accept flexible student details such as name, age and city."

### Remember

- `*args` → Positional arguments
- Tuple
- `**kwargs` → Keyword arguments
- Dictionary
- Flexible functions

### Follow-up

**Q:** Are args and kwargs reserved Python keywords?

No. They are conventional names. The important parts are the * and ** operators.
