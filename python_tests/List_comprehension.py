numCount = 4;

test = ['key1 45 set mado der','key2 deer meo dso ados','key3 hanno dueo set net tassle', 'key4 78 maybe herro dadyy']

masterlist = []
counter = 0

def valuecheck(identifer):
	try:
		(int(identifer))
		return True
	except ValueError:
		return False

for items in test:
	rows = items.split(",")[0]
	identifer = rows.split()[1]
	flag = valuecheck(identifer)
	if(flag):
		masterlist.append(rows)
	else:
		counter+=1
		masterlist.insert(0,rows)


masterlist[0:counter] = sorted(masterlist[0:counter])
print("\n".join(masterlist))
		