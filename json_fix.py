import json
import ast

with open('database.txt', 'r') as f:
	text = f.read()

tt = text.split(']\n[')
dict_strings = [item for item in tt if len(item) > 2]
dicts = [ast.literal_eval(item) for item in dict_strings]

combined_array = []
for item in dicts:
	combined_array.extend(item)

j = json.dumps(combined_array, indent=2)

with open('fixed.txt', 'w') as o:
	o.write(j)
