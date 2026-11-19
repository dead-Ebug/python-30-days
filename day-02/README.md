# Day 2 · Variables and Data Types

On Day 1 you used `print()` to show a message. Today you’ll give values names, see how Python treats different kinds of values, and pull individual items out of lists, tuples, and dictionaries.

## 1. Give a value a name

Think of a variable as a sticky note with a name on it. In `name = "John"`, the sticky note says `name` and points to the value `"John"`. The equals sign performs an **assignment**. Read it from right to left as “give the value on the right the name on the left.”

```python
name = "John"

print(name)    # John
print("name")  # name
```

Python looks up a variable when you write its name by itself. Quotes tell Python to use the text exactly as written.

## 2. Check what kind of value you have

A **data type** describes the kind of value Python is working with. The number `30` can be used for arithmetic. The text `"30"` might be what you see printed on a jersey.

| Type | Example | What it represents |
| --- | --- | --- |
| String (`str`) | `"John"` | Text, such as someone’s name |
| Integer (`int`) | `30` | A whole number, such as an age |
| Float (`float`) | `6.1` | A number that can represent a fractional amount, such as a measurement |
| List (`list`) | `["apple", "banana", "cherry"]` | An ordered group you can update |
| Tuple (`tuple`) | `(3, 4)` | An ordered group with fixed item slots |
| Dictionary (`dict`) | `{"name": "Alice", "age": 25}` | Values stored under labels called keys |

Use `type()` to check the type of a value. With two strings, `+` joins the text. With two integers, it adds the numbers.

```python
print(type("30"))  # <class 'str'>
print(type(30))    # <class 'int'>
print(type(30.0))  # <class 'float'>
print("30" + "1")  # 301
print(30 + 1)      # 31
```

If you try `"30" + 1`, Python raises a `TypeError` because this operation mixes a string and an integer.

## 3. Use an index with a list or tuple

An **index** is a position. Picture three fruits lined up on a shelf. Python starts counting positions at `0`.

| Index | Position | Fruit |
| --- | --- | --- |
| `0` | First | Apple |
| `1` | Second | Banana |
| `2` | Third | Cherry |

### Lists let you replace an item

Read `fruits[1]` as “the item in position 1.” Put that expression to the left of `=` when you want to replace the item in that slot.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[1])  # banana

fruits[1] = "mango"
print(fruits)     # ['apple', 'mango', 'cherry']
```

### Tuples have fixed slots

Think of `(3, 4)` as two coordinates printed on a map. You can read either coordinate by its index. Python calls a tuple **immutable**, which means its slots are fixed once it is created. Trying `point[0] = 7` would raise a `TypeError`. You can assign a whole new tuple to the name `point`, like swapping one printed map for another.

```python
point = (3, 4)
print(point[0])  # 3

point = (7, 4)
print(point[0])  # 7
```

## 4. Use a key with a dictionary

Picture a contact card with a field named `name` and another named `age`. In a dictionary, each label is a **key**, and the information next to it is its **value**. Read `person["name"]` as “look up the value under the key `"name"`.”

```python
person = {"name": "Alice", "age": 25}

print(person["name"])  # Alice
person["age"] = 26
print(person["age"])   # 26
```

In `fruits[1]`, the brackets contain a position. In `person["name"]`, they contain a text key. If you write `person[name]` and the variable `name` contains `"John"`, Python looks for the key `"John"`. That key is missing here, so Python raises a `KeyError`.

## 5. Give a name a new value

Imagine a scoreboard that displays `10` right now and `"pending"` later. **Reassignment** means giving an existing name a new value. Python allows that new value to have a different type. This is part of **dynamic typing**.

```python
score = 10
print(score)        # 10
print(type(score))  # <class 'int'>

score = "pending"
print(score)        # pending
print(type(score))  # <class 'str'>
```

## Run the examples and try the practice

In VS Code, open the extracted `day-02` folder. Select **Terminal → New Terminal** to open the panel where you type commands. Run the first command to see the lesson examples. Then open `practice.py`, add your answers under the comments, and save. Run the second command to check what your code prints.

```powershell
python examples.py
python practice.py
```

On Windows, if `python` is unavailable and you have the Python launcher installed, replace `python` with `py` in those commands.
