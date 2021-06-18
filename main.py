import json

f = open('todo.json').read()

data = json.loads(f)
print(data)