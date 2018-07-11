import re
from collections import Counter

my_string= "My bologna has a first name, it is O-s-c-a-r. My bologna has a second name, it is M-e-y-e-r. Oh, I love to eat it every day, and if you ask me why, I willl say: cuz Oscar Meyer has a way with b-o-l-o-g-n-a. How iss that? Extraordinary crimes against the people and the state had to be avenged by agents extraordinary. Two such people are John Steed, top professional; and his partner, Emma Peel, talented amateur... otherwise known as The Avengers. Lady Godiva was a freedom rider, she did not care if the whole world looked. Joan of Arc with the Lord to guide her, she was a sister who really cooked. Isadora was the first bra burner, are not you glad she showed up. And when the country was falling apart Betsy Ross got it all sewed up. And then there is Maude. That old compromising, enterprisin, anything but tranquilizing, right-on Maude."

words = re.findall(r'\w+',my_string)
all_words = [word.upper() for word in words]
dict_words= (all_words).sort(reverse=True)

for x in dict_words:
	print (x, ': ',dict_words[x])