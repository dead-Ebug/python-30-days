# Day 1 · Introduction to Python

Today you’ll run your first Python program, read each instruction, and predict what appears on the screen.

## What is Python?

Python is a programming language, a way to write instructions a computer can follow. Think of a program as a recipe. The recipe describes the steps, and someone follows them. The **Python interpreter** is the software that runs your Python program.

Python is a **high-level** language. One short instruction can display a message without you having to tell the computer how to draw each letter. Python is often called **interpreted** because an interpreter runs your program. People use Python to build websites, analyze data, automate repetitive tasks, and work with AI.

## 1. Say hello

Open [hello_world.py](hello_world.py) to see your first program.

```python
# Display a greeting
print("Hello, World!")
```

The text the program displays is called **output**. Here’s what you’ll see.

```text
Hello, World!
```

| Piece | What it does |
| --- | --- |
| `# Display a greeting` | A **comment** is a note for whoever reads the code. A `#` outside a string starts a comment that runs to the end of that line. |
| `print` | A built-in **function**. A function is a reusable action. This one displays what you give it. |
| `(...)` | The parentheses hold what you give to the function. Here that’s the greeting. |
| `"Hello, World!"` | A **string** is a piece of text. The quotes mark where the text starts and ends. The output shows the text inside the quotes. |

Think of a comment as a cook’s note in the margin of a recipe. Keep `print(...)` on its own line. If you place it after `#` on the same line, Python treats it as part of the comment and skips it.

## 2. Follow two instructions in order

Open [cereal_steps.py](cereal_steps.py). Predict which line will appear first.

```python
print("Pour the cereal.")
print("Add the milk.")
```

```text
Pour the cereal.
Add the milk.
```

In this simple sequence, Python runs the first `print()` call before the second. Reading from top to bottom helps you trace the order.

## Run the examples on Windows

With Python 3 installed, open the `day-01` folder in File Explorer. Click the address bar, type `powershell`, and press Enter. This opens PowerShell in that folder.

Run these commands one at a time. Each asks Python to run the named file.

```powershell
python hello_world.py
python cereal_steps.py
```

If Windows can’t find `python`, try `py -3 hello_world.py` and `py -3 cereal_steps.py`.

## Try it yourself

1. In `hello_world.py`, change the text inside the quotes to a greeting of your own. Predict what will appear, then save and run the file again.
2. In `cereal_steps.py`, swap the two `print()` lines. Predict the new order, then save and run the file to check.
