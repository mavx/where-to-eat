import json
import ast

with open('database.txt', 'r') as f:
	text = f.read()

tt = text.split('},{')
l = len(tt)
d = [] 
for i in tt:
	if i == tt[0]:
		i = i+'}'
		# print('First esntry processed')
	elif i == tt[-1]:
		i = '{'+i
		# print('Last entry processed')
	else:		
		i = '{'+i+'}'
	# 	print('Processing...')
	# print('Converting data to json')
	j = json.loads(i)
	# print('Adding to dictionary')
	d.append(j)


# ttt = json.loads(tt)

# dict_strings = [item for item in tt if len(item) > 2]
# dicts = [ast.literal_eval(item) for item in dict_strings]

# combined_array = []
# for item in dicts:
# 	combined_array.extend(item)

# j = json.dumps(combined_array, indent=2)

# with open('fixed.txt', 'w') as o:
# 	o.write(ttt)

j = json.dumps(d, indent= 2)

with open('database.json', 'w') as fp:
	fp.write(j)