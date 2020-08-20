import json

with open('json_test.json', encoding='utf8') as f:
    test = json.load(f)

print(test)
print(type(test))

with open('to_json_test2.json', 'w', encoding='utf8') as f:
    json.dump(test, f, ensure_ascii=False, indent=4)


with open('to_json_test2.json', encoding='utf8') as f:
    print(f.read())