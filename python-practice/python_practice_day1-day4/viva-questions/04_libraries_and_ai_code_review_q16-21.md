# Viva answers: Questions 16-21: Libraries and AI code review

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q16. What is the difference between NumPy arrays and traditional Python lists?

### Concept

Python lists are general-purpose collections that can store different types of objects. NumPy arrays are designed for numerical computation and generally store elements of the same data type.

NumPy arrays are usually more efficient for large numerical operations.

### How it works

| Python List | NumPy Array |
|---|---|
| Can contain different data types | Usually homogeneous data type |
| General-purpose | Numerical computation |
| Mathematical operations often require loops | Supports vectorized operations |
| Generally higher overhead for numerical data | Generally more memory and computationally efficient |
| No direct element-wise arithmetic behavior | Supports element-wise arithmetic |

### Example

```python
import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5, 6]

array1 = np.array(list1)
array2 = np.array(list2)

print(array1 + array2)
```

**Output:**

```text
[5 7 9]
```

With Python lists:

```python
print(list1 + list2)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

Here, list addition concatenates the lists, while NumPy performs element-wise addition.

### Interview answer

> "Python lists are general-purpose collections that can store different types of objects, while NumPy arrays are mainly designed for numerical computation and generally contain elements of the same data type. NumPy supports vectorized operations, which allow us to perform mathematical operations on entire arrays efficiently. For example, adding two NumPy arrays performs element-wise addition, whereas adding two Python lists concatenates them."

### Remember

- List → General-purpose
- NumPy → Numerical computation
- Homogeneous data
- Vectorization
- Element-wise operations

### Follow-up

**Q:** What is vectorization?

**Hint:** Performing an operation on an entire array without explicitly writing a Python loop for each element.

## Q17. What is Pandas? What is the difference between Series and DataFrame?

### Concept

Pandas is a Python library used for data manipulation, analysis, and handling structured data.

It provides two important data structures:

- Series: One-dimensional labeled data.
- DataFrame: Two-dimensional tabular data consisting of rows and columns.

### How it works

Pandas is useful for:

- Reading CSV and Excel files.
- Cleaning data.
- Handling missing values.
- Filtering records.
- Grouping and aggregating data.
- Performing exploratory data analysis.

### Comparison

| Series | DataFrame |
|---|---|
| One-dimensional | Two-dimensional |
| Single labeled sequence | Rows and columns |
| Similar to one column | Similar to a table |
| Can contain one data type generally | Different columns can have different types |

### Example

```python
import pandas as pd

data = {
    "Name": ["Nishant", "Rahul", "Aman"],
    "Age": [23, 22, 24],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
```

**Output:**

```text
      Name  Age  Marks
0  Nishant   23     85
1   Rahul   22     90
2     Aman   24     78
```

A Series:

```python
ages = pd.Series([23, 22, 24])

print(ages)
```

### Interview answer

> "Pandas is a Python library used for data manipulation and analysis. It provides two major data structures: Series and DataFrame. A Series is a one-dimensional labeled data structure, while a DataFrame is a two-dimensional structure containing rows and columns. For example, if I load student records containing names, ages and marks from a CSV file, I can use a DataFrame to filter students, calculate averages and analyze the data."

### Remember

- Pandas → Data analysis
- Series → 1D
- DataFrame → 2D
- CSV/Excel handling
- Cleaning and analysis

### Follow-up

**Q:** How do you read a CSV file using Pandas?

**Hint:** 

```python
df = pd.read_csv("data.csv")
```

## Q18. What is Matplotlib? What types of visualizations can we create using it?

### Concept

Matplotlib is a Python library used to create visualizations and graphical representations of data.

It helps us understand patterns, trends, distributions and relationships in data.

### How it works

Common visualizations include:

| Chart | Purpose |
|---|---|
| Line chart | Trends over time |
| Bar chart | Comparing categories |
| Histogram | Distribution of numerical data |
| Scatter plot | Relationship between two variables |
| Pie chart | Proportions |
| Box plot | Distribution and outliers |

### Example

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 200]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

This creates a line graph showing the sales trend over four months.

### Practical example

If we want to understand a company's monthly sales:

- Line chart → See trends.
- Bar chart → Compare individual months.
- Histogram → Analyze the distribution of sales values.

### Interview answer

> "Matplotlib is a Python library used to visualize data through graphs and charts. It helps us identify trends, comparisons, distributions and relationships in datasets. Common visualizations include line charts, bar charts, histograms, scatter plots and pie charts. For example, I can use a line chart to visualize monthly sales and identify whether sales are increasing or decreasing over time."

### Remember

- Matplotlib → Data visualization
- Line → Trend
- Bar → Comparison
- Histogram → Distribution
- Scatter → Relationship

### Follow-up

**Q:** What is the difference between a bar chart and a histogram?

**Hint:** Bar charts compare categories, while histograms show the distribution of continuous numerical data grouped into intervals.

## Q19. If an AI generates a Python program, how would you review it to determine whether it is correct?

### Concept

AI-generated code should be treated as a draft, not automatically as correct code.

We should verify that it meets the requirements, produces correct results, handles edge cases and behaves as expected.

### How it works

My review process would be:

1. Understand the requirement.
2. Read the code and understand its logic.
3. Check whether the logic solves the problem.
4. Test normal cases.
5. Test edge cases.
6. Check the output against expected results.
7. Look for errors or unnecessary complexity.

### Example

Suppose AI generates a function to find the largest number in a list.

```python
def largest(numbers):
    return max(numbers)
```

I would test:

```python
print(largest([10, 20, 5]))  # 20
print(largest([-5, -2, -10])) # -2
```

But I would also consider:

```python
largest([])
```

The empty list causes an error. So I need to determine how the program should handle empty input and update the code accordingly.

### Interview answer

> "I wouldn't blindly trust AI-generated code. First, I would understand the requirement and review the code's logic. Then I would test it with normal inputs, edge cases and invalid inputs, and compare the outputs with the expected results. I would also check whether it handles errors properly and whether the implementation is readable and efficient. For example, if AI generates a function to find the largest number, I would test normal values, negative numbers and an empty list to identify possible issues."

### Remember

- Understand requirements
- Review logic
- Test normal cases
- Test edge cases
- Verify expected output

### Follow-up

**Q:** What are edge cases?

**Hint:** Inputs at unusual boundaries or special conditions, such as empty lists, zero, negative numbers, very large values or invalid input.

## Q20. If an AI tool generates a program, what would you check before approving the code?

### Concept

AI can generate code quickly, but the code may contain logical mistakes, bugs, security issues, or inefficient implementations.

Before approving AI-generated code, I should verify that it is correct, safe, readable, and suitable for the requirements.

### How it works

I would check:

1. Correctness: Does it solve the actual problem?
2. Testing: Does it pass test cases?
3. Edge cases: Does it handle unusual inputs?
4. Security: Does it introduce vulnerabilities?
5. Performance: Is it efficient enough?
6. Readability: Can another developer understand it?
7. Maintainability: Is it easy to modify in the future?

### Example

Suppose AI generates a login function:

```python
def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False
```

Before approving it, I would notice that credentials are hardcoded. That is a security concern.

I would also consider whether passwords should be stored securely, whether input validation is needed, and whether the authentication system should use a proper database and password hashing.

### Interview answer

> "Before approving AI-generated code, I would review it against the requirements and check its correctness, testing, edge cases, security, performance and readability. I would run test cases, inspect the logic, and verify that it doesn't contain hardcoded credentials or unsafe operations. For example, if AI generates a login function, I would check whether passwords are handled securely rather than being hardcoded directly into the program."

### Remember

- Correctness
- Testing
- Edge cases
- Security
- Performance and maintainability

### Follow-up

**Q:** Would you directly use AI-generated code in production?

**Hint:** Only after appropriate review, testing, validation, and security checks.

## Q21. Explain with an example how you would check code for security, performance, and maintainability.

### Concept

When reviewing code, I don't only check whether it works. I also check three important qualities:

- Security: Can the code be exploited or expose sensitive information?
- Performance: Does the code execute efficiently and use resources appropriately?
- Maintainability: Can another developer easily understand, debug, and modify it?

These three qualities help ensure code is suitable for real-world use, not just a successful test run.

### How it works

| Aspect | What I Check |
|---|---|
| Security | Hardcoded secrets, unsafe input, SQL injection, permissions |
| Performance | Unnecessary loops, repeated calculations, memory usage |
| Maintainability | Readability, naming, modularity, comments where useful |

### Example

Suppose AI generates this Python code to search for a user in a database:

```python
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return execute_query(query)
```

Security check: The query directly concatenates user input, which could create SQL injection vulnerabilities.

Performance check: If the application repeatedly executes the same query, I would examine whether unnecessary database calls or inefficient queries are occurring.

Maintainability check: I would check whether the function has a clear name, whether database logic is properly separated, and whether error handling is present.

A safer approach would use parameterized queries:

```python
def get_user(username):
    query = "SELECT * FROM users WHERE username = ?"
    return execute_query(query, (username,))
```

### Interview answer

> "I review code from three perspectives: security, performance and maintainability. For security, I check for issues such as hardcoded credentials, unsafe input handling and SQL injection. For performance, I look for unnecessary loops, repeated operations and excessive memory usage. For maintainability, I check whether the code is readable, modular and easy to modify. For example, if AI generates a database query by concatenating user input, I would identify the SQL injection risk and replace it with a parameterized query."

### Remember

- Security → Protect data and prevent vulnerabilities
- Performance → Efficient execution
- Maintainability → Easy to understand and modify
- SQL injection → Unsafe user input
- Parameterized query → Safer database interaction

### Follow-up

**Q:** What is SQL injection?

**Hint:** It occurs when malicious SQL is inserted through user input and improperly incorporated into a database query, potentially allowing an attacker to manipulate the query.
