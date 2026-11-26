# Viva answers: Questions 36-40: Async, frameworks, APIs and Big O

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q36. What is the difference between synchronous and asynchronous programming?

### Concept

Both are ways of executing tasks in a program, but they differ in how they handle waiting.

Synchronous programming: Tasks execute one after another. The next operation generally waits until the current operation finishes.

Asynchronous programming: A task can pause while waiting for an operation to complete, allowing other tasks to make progress in the meantime.

Think about ordering food at a restaurant:

- Synchronous: You wait at the counter until your order is ready before doing anything else.
- Asynchronous: You place your order, receive a token and do other things while your food is being prepared.

### How it works

| Synchronous | Asynchronous |
|---|---|
| Sequential execution | Allows overlapping operations |
| Waiting blocks the current flow | Can switch to other tasks while waiting |
| Simpler to understand | Requires async programming concepts |
| Suitable for straightforward tasks | Useful for I/O-bound operations |
| Uses normal function calls | Uses mechanisms like async and await |

Asynchronous programming is particularly useful when an application performs many operations involving:

- API requests
- Network communication
- Database queries
- File operations

### Example

Synchronous example:

```python
import time

def task1():
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 completed")

task1()
task2()
```

**Output:**

```text
Task 1 completed
Task 2 completed
```

Task 2 starts only after Task 1 finishes.

Asynchronous example:

```python
import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

**Output:**

```text
Task 2 completed
Task 1 completed
```

Here, while Task 1 is waiting, Task 2 gets an opportunity to execute.

### Interview answer

> "Synchronous programming executes operations sequentially, where the next operation generally waits for the previous one to finish. Asynchronous programming allows a task to pause during waiting operations so that other tasks can make progress. For example, if an application needs to make multiple API requests, asynchronous programming can handle other requests while one is waiting for a response. It is particularly useful for I/O-bound applications."

### Remember

- Synchronous → Sequential execution
- Asynchronous → Non-blocking waiting
- asyncio
- API and network requests
- I/O-bound operations

### Follow-up

**Q:** Does asynchronous programming mean that multiple tasks execute simultaneously?

Not necessarily. Asynchronous programming enables concurrency, but it does not automatically mean parallel execution on multiple CPU cores.

## Q37. What is the difference between async, def, and await in Python?

### Concept

These are keywords used in Python's asynchronous programming.

- def → Defines a normal function.
- async def → Defines a coroutine function.
- await → Pauses the coroutine until an awaitable operation produces its result, allowing the event loop to run other tasks.

The important thing to understand is that async def creates a coroutine function, while await is used inside an asynchronous function to wait for an awaitable operation.

### How it works

Consider this sequence:

1. Define an asynchronous function using async def.
2. Call an awaitable operation using await.
3. The coroutine suspends while waiting.
4. The event loop can execute other ready tasks.
5. Once the awaited operation completes, execution resumes.

### Example

```python
import asyncio

async def get_data():
    print("Fetching data")

    await asyncio.sleep(2)

    print("Data received")

async def main():
    await get_data()

asyncio.run(main())
```

**Output:**

```text
Fetching data
Data received
```

Let's understand each keyword:

| Code | Meaning |
|---|---|
| async def get_data() | Defines a coroutine function |
| await asyncio.sleep(2) | Waits without blocking the event loop |
| async def main() | Defines the main coroutine |
| asyncio.run(main()) | Starts and runs the event loop |

**Important:** Calling an async def function normally creates a coroutine object. It doesn't execute the coroutine to completion automatically. It must be awaited or scheduled.

### Interview answer

> "In Python, def is used to define a normal function, while async def defines a coroutine function for asynchronous programming. The await keyword is used inside an asynchronous function to wait for an awaitable operation without blocking the event loop. For example, when making an API request, I can use await while waiting for the response, allowing other asynchronous tasks to execute in the meantime."

### Remember

- def → Normal function
- async def → Coroutine function
- await → Wait for an awaitable
- Event loop → Manages asynchronous tasks
- asyncio.run() → Runs a coroutine

### Follow-up

**Q:** Can we use await inside a normal function?

No, not directly. await is normally used inside an async def function. Python also supports top-level await in certain interactive environments.

## Q38. What are Django, Flask and FastAPI?

### Concept

Django, Flask and FastAPI are Python web frameworks used to build web applications and backend services, but they differ in their features and design approaches.

A framework provides ready-made tools and structures so developers don't have to build everything from scratch.

### How it works

Let's understand each framework.

#### Django

A full-featured web framework that provides many built-in features.

- Authentication
- Database ORM
- Admin panel
- URL routing
- Security features

Best suited for larger web applications requiring many built-in capabilities.

#### Flask

A lightweight microframework that provides the essentials and allows developers to choose additional components.

- Simple structure
- Flexible
- Lightweight
- Easy to get started

Best suited for smaller applications and lightweight services.

#### FastAPI

A modern framework focused on building APIs, with support for asynchronous programming and automatic API documentation.

- High performance
- Type hints
- Automatic validation
- OpenAPI documentation
- Async support

Best suited for modern API services and backend applications.

### Comparison

| Feature | Django | Flask | FastAPI |
|---|---|---|---|
| Type | Full-stack framework | Microframework | API framework |
| Structure | More built-in features | Minimal | API-focused |
| Async support | Supported | Supported through async views, with limitations | Strong async support |
| Learning curve | Moderate | Easy to start | Moderate |
| Common use | Web applications | Small apps and services | APIs and backend services |

### Practical example

Suppose we are developing a student management application.

- Django: We can build the complete application with authentication, database models and an admin panel.
- Flask: We can build a small student registration application with only the components we need.
- FastAPI: We can build an API that returns student information in JSON format to a mobile application.

### Interview answer

> "Django, Flask and FastAPI are Python web frameworks used for backend development. Django is a full-featured framework that provides built-in functionality such as authentication, ORM and an admin panel. Flask is a lightweight microframework that gives developers more flexibility. FastAPI is a modern framework mainly used for building APIs, with support for asynchronous programming, type hints and automatic documentation. For example, I would choose Django for a complete web application and FastAPI for a modern API-based backend."

### Remember

- Django → Full-featured
- Flask → Lightweight and flexible
- FastAPI → Modern API development
- ORM → Database interaction
- API → Communication between applications

### Follow-up

**Q:** What is ORM in Django?

ORM stands for Object Relational Mapping. It allows developers to interact with databases using Python classes and objects instead of writing SQL queries for every operation.

## Q39. What is an API?

### Concept

API stands for Application Programming Interface.

An API is a mechanism that allows two software applications or components to communicate with each other through defined rules and interfaces.

Think of an API as a waiter in a restaurant.

- You are the customer.
- The kitchen is the server.
- The waiter is the API.

You place an order with the waiter, the waiter communicates with the kitchen, and then brings back the result.

### How it works

Consider a weather application on your phone.

1. You open the weather application.
2. It sends a request to a weather API.
3. The API communicates with the weather server.
4. The server processes the request.
5. The API returns weather information.
6. Your application displays the result.

A common type is a REST API, which often uses HTTP methods:

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create data |
| PUT | Replace or update a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

### Example

Suppose we have a student management application.

A client sends:

GET /students/101

The server may respond with:

```python
{
    "id": 101,
    "name": "Nishant",
    "age": 23
}
```

The client receives the student information without needing direct access to the server's internal database.

### Interview answer

> "API stands for Application Programming Interface. It allows different software applications to communicate with each other through predefined rules and interfaces. For example, when a weather application needs current weather information, it sends a request to a weather API, which processes the request and returns the data. REST APIs commonly use HTTP methods such as GET, POST, PUT, PATCH and DELETE to perform different operations."

### Remember

- API → Application Programming Interface
- Communication between applications
- Request and response
- REST API
- HTTP methods: GET, POST, PUT, PATCH, DELETE

### Follow-up

**Q:** What is the difference between GET and POST?

- GET retrieves information from a server.
- POST sends data to a server, commonly to create a resource or trigger an operation.

## Q40. What is Time Complexity? Why should a Python developer understand Big O notation when choosing data structures?

### Concept

Time complexity describes how the execution time of an algorithm grows as the input size increases.

Big O notation is used to express this growth rate.

It helps us understand whether an algorithm will remain efficient when the amount of data becomes larger.

For example, searching for a number in a list of 10 elements is relatively easy. But what if the list contains 10 million elements?

We need to consider how the algorithm scales.

### How it works

Let's understand the most common complexities:

| Big O | Name | Meaning |
|---|---|---|
| O(1) | Constant | Execution doesn't grow with input size |
| O(log n) | Logarithmic | Growth is very slow |
| O(n) | Linear | Grows proportionally with input |
| O(n log n) | Linearithmic | Common in efficient sorting |
| O(n^2) | Quadratic | Often occurs with nested loops |
| O(2^n) | Exponential | Grows very rapidly |

### Example

Let's compare searching in a Python list and dictionary.

#### A. Searching in a list

```python
numbers = [10, 20, 30, 40, 50]

target = 40

for num in numbers:
    if num == target:
        print("Found")
        break
```

Time complexity: O(n) in the worst case.

Why? We may need to check every element.

#### B. Searching in a dictionary

```python
students = {
    101: "Nishant",
    102: "Rahul",
    103: "Aman"
}

print(students.get(102))
```

Average-case time complexity: O(1).

Why? Dictionary lookup uses hashing to locate the value without scanning every entry.

### Why a Python developer needs Big O

Because choosing the correct data structure can significantly affect application performance.

| Data Structure | Common Operation | Average/Worst Complexity |
|---|---|---|
| List | Access by index | O(1) |
| List | Search by value | O(n) |
| List | Append | Amortized O(1) |
| Dictionary | Key lookup | Average O(1) |
| Set | Membership check | Average O(1) |

For example, if I frequently check whether an element exists in a collection, a set or dictionary is often more suitable than repeatedly searching through a list.

### Interview answer

> "Time complexity describes how an algorithm's execution time grows with the input size, and Big O notation helps us represent that growth. It is important because it helps developers choose efficient algorithms and data structures. For example, searching for an element in a list takes O(n) time in the worst case, whereas dictionary key lookup takes O(1) time on average. So, if my application performs frequent lookups, using a dictionary can be more efficient than using a list."

### Remember

- Time complexity → Algorithm efficiency
- Big O → Growth rate
- O(1) → Constant
- O(n) → Linear
- O(n^2) → Quadratic
- Choose data structures based on operations

### Follow-up

**Q:** What is the difference between time complexity and space complexity?

- Time complexity measures how execution time grows with input size.
- Space complexity measures how memory requirements grow with input size.

For example, an algorithm that creates an additional list to store results may require O(n) auxiliary space.
