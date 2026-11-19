# Day 2 examples. Run this file to see each section in order.

print("1. Give a value a name")
name = "John"
print(name)
print("name")

print("\n2. Check data types")
print(type("30"))
print(type(30))
print(type(30.0))
print("30" + "1")
print(30 + 1)

print("\n3. Use an index with a list or tuple")
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
fruits[1] = "mango"
print(fruits)

point = (3, 4)
print(point[0])
point = (7, 4)
print(point[0])

print("\n4. Use a key with a dictionary")
person = {"name": "Alice", "age": 25}
print(person["name"])
person["age"] = 26
print(person["age"])

print("\n5. Give a name a new value")
score = 10
print(score)
print(type(score))
score = "pending"
print(score)
print(type(score))
