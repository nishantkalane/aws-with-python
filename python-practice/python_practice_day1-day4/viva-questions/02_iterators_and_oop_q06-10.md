# Viva answers: Questions 6-10: Iterators and OOP

Speaking pattern for every answer: **Definition -> How it works -> Example -> Practical importance.**
Do not memorise the paragraph word for word; learn the idea, then say it in your own words.

## Q6. What is an iterator? Explain with an example.

### Concept

An iterator is an object that allows us to access elements of a collection one at a time.

Instead of accessing all elements at once, an iterator keeps track of its current position and provides the next element when requested.

### How it works

Python iterators use two methods:

- iter() → Returns an iterator.
- next() → Returns the next element.

An iterator follows the iterator protocol, which means it implements `__iter__()` and `__next__()`.

### Example

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

The iterator remembers where it stopped. Each call to next() moves forward.

### Interview answer

> "An iterator is an object that allows us to access elements one at a time while maintaining its current position. In Python, we use iter() to create an iterator and next() to retrieve the next element. For example, if I create an iterator from a list containing 10, 20 and 30, each call to next() returns the next value without restarting from the beginning."

### Remember

- Iterator → Sequential access
- iter() → Create iterator
- next() → Retrieve next element
- Maintains state
- StopIteration when exhausted

### Follow-up

**Q:** What is the difference between an iterable and an iterator?

**Hint:** An iterable can provide an iterator; an iterator is the object that actually keeps track of iteration state.

## Q7. What is the difference between a class and an object? How do we create objects in Python?

### Concept

A class is a blueprint that defines the properties and behavior of something.

An object is an actual instance created from that class.

Think of a class as a blueprint for a house. The blueprint describes the design, but the actual houses built using it are objects.

### How it works

A class can contain:

- Attributes → Data or properties
- Methods → Functions defined inside a class

Objects are created by calling the class.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


student1 = Student("Nishant", 23)
student2 = Student("Rahul", 22)

student1.display()
student2.display()
```

Here:

- Student → Class
- student1 and student2 → Objects
- name and age → Attributes
- display() → Method

Each object has its own data.

### Interview answer

> "A class is a blueprint that defines the attributes and methods of an entity, whereas an object is an actual instance of that class. In Python, we create objects by calling the class name. For example, a Student class may contain name and age attributes and a display method. We can create multiple student objects from the same class, each having different data."

### Remember

- Class → Blueprint
- Object → Instance
- Attributes → Data
- Methods → Behavior
- ClassName() → Object creation

### Follow-up

**Q:** What is self in Python?

**Hint:** It refers to the current instance of the class and allows us to access that object's attributes and methods.

## Q8. What is the difference between `__init__()` and `__new__()`?

### Concept

Both are special methods involved in object creation, but they perform different jobs.

- `__new__()` → Creates and returns the object.
- `__init__()` → Initializes the object's attributes after it has been created.

### How it works

The object creation process is approximately:

1. Python calls `__new__()`.
2. `__new__()` creates the object.
3. Python calls `__init__()` on that object.
4. The object becomes ready for use.

### Example

```python
class Student:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")
        self.name = "Nishant"


student = Student()
```

**Output:**

```text
Creating object
Initializing object
```

### Interview answer

> "`__new__()` and `__init__()` are both special methods used during object creation. `__new__()` is responsible for creating and returning the object, while `__init__()` initializes the object's attributes after creation. Normally, we work with `__init__()` when defining classes, while `__new__()` is used in more specialized situations such as controlling object creation or working with immutable types."

### Remember

- `__new__()` → Creates object
- `__init__()` → Initializes object
- `__new__()` runs first
- `__init__()` runs second
- `__new__()` returns the instance

### Follow-up

**Q:** Why is `__new__()` particularly important for immutable objects?

**Hint:** Immutable objects cannot be modified after creation, so their value must be established during the creation process.

## Q9. Explain inheritance and the different types of inheritance supported in Python.

### Concept

Inheritance allows one class to acquire properties and methods from another class.

It promotes code reuse and helps create relationships between classes.

The existing class is called the parent/base class, and the class that inherits from it is called the child/derived class.

### How it works

Python supports several forms of inheritance:

| Type | Meaning |
|---|---|
| Single | One child inherits from one parent |
| Multiple | One child inherits from multiple parents |
| Multilevel | A class inherits from a class that itself inherits from another class |
| Hierarchical | Multiple child classes inherit from the same parent |
| Hybrid | Combination of multiple inheritance types |

### Example

```python
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.eat()
dog.bark()
```

Dog inherits the eat() method from Animal, so we don't need to redefine it.

### Interview answer

> "Inheritance is an OOP concept where one class acquires the attributes and methods of another class. It helps with code reuse and creating logical relationships between classes. Python supports single, multiple, multilevel, hierarchical and hybrid inheritance. For example, a Dog class can inherit from an Animal class and reuse its eat() method while adding its own behavior, such as barking."

### Remember

- Parent/base class
- Child/derived class
- Code reuse
- class Child(Parent):
- Five common inheritance types

### Follow-up

**Q:** What is multiple inheritance in Python?

**Hint:** One class can inherit from more than one parent class.

## Q10. What is the difference between method overloading and method overriding?

### Concept

Both are related to polymorphism, but they work differently.

- Method overloading: Multiple methods with the same name but different parameter signatures.
- Method overriding: A child class provides its own implementation of a method inherited from its parent class.

### Comparison

| Method Overloading | Method Overriding |
|---|---|
| Same method name, different parameters | Same method name in parent and child |
| Usually occurs within the same class | Occurs through inheritance |
| Compile-time concept in languages like Java | Runtime polymorphism |
| Python doesn't support traditional overloading directly | Python supports overriding |

### Example: Overriding

```python
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()
dog.sound()
```

**Output:**

```text
Bark
```

The child class overrides the parent method.

### Python-style overloading alternative

Python commonly handles different arguments using default parameters or `*args`.

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(2, 3))
print(calc.add(2, 3, 4))
```

### Interview answer

> "Method overloading means having methods with the same name but different parameter lists, while method overriding means a child class provides a new implementation of a method inherited from its parent. Python does not support traditional method overloading in the same way as Java, but we can achieve similar behavior using default arguments or `*args`. Python supports method overriding directly through inheritance."

### Remember

- Overloading → Same name, different parameters
- Overriding → Child changes inherited behavior
- Python has no traditional signature-based overloading
- Default parameters and `*args` can achieve similar behavior
- Overriding → Inheritance

### Follow-up

**Q:** Does Python support method overloading?

**Hint:** Not traditional method overloading based on parameter signatures. Defining the same method name multiple times in a class replaces the previous definition.
