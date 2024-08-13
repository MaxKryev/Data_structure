human = {"name": "Максим", "age": 31, "sex": "мужской", "height": 175, "weight": 85}
print(human["name"], human["age"], human["sex"], human["height"], human["weight"])
human["foot"] = 42
print(human)
del human["age"]
print(human)