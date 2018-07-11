from collections import Counter
import operator

list1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi iaculis justo vel massa laoreet semper. Vestibulum vitae suscipit elit. Nulla lacinia sed lorem eu tempor. Morbi et nulla nibh. Mauris quis cursus urna. Nam libero ex, tempus vel risus eu, blandit dictum mi. Duis non dolor a elit euismod ornare. Vivamus imperdiet, augue ut pharetra cursus, ligula arcu eleifend est, sed tincidunt justo turpis sit amet nisi. Proin lacus ipsum, finibus sed elit eget, accumsan eleifend quam. Maecenas mollis eros vel nibh semper vestibulum. Aliquam semper vel urna sit amet cursus. Fusce lobortis, dolor et egestas porta, tortor lectus feugiat.'

counts = dict()
words = list1.split()

for word in words:
	if word in counts:
		counts[word]+=1
	else:
		counts[word] =1 


sorted_counts = dict(sorted(counts.items(),key=operator.itemgetter(1), reverse = True))
for k,v in sorted_counts.items():
	print(k,":",v)
