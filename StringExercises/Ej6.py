sentence = input("Sentence: ")
vowel = ''
while vowel.lower() not in ('a','e','i','o','u'):
	vowel = input("Vowel: ")
sentence = sentence.replace(vowel,vowel.upper())
print(sentence)
