def greeting(name):
    print("Hello", name)

person = [
  {
    "name": "John",
    "age": 36,
    "country": "Norway"
  },
  {
    "name": "Anna",
    "age": 32,
    "country": "Sweden"
  },
  {
    "name": "Peter",
    "age": 28,
    "country": "Denmark"
  },
  {
    "name": "Linda",
    "age": 29,
    "country": "Norway"
  },
  {
    "name": "Lars",
    "age": 35,
    "country": "Sweden"
  }
]

for i in range(0, len(person)):
    greeting(person[i]["name"])
