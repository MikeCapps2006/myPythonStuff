import re

text = 'The cool kids are in cool school'

pattern = 'cool'

match = re.search(pattern, text) #looks for first occurance of pattern
matches = re.findall(pattern, text) #makes all occurances in a list 

print(match)
print(matches)

for found in re.finditer(pattern, text): #iterates over the occuranaces of pattern
    print(found.span())

#regex practice

phone_number = 'This is my phone number: 843-798-0019'
regex_for_phone_number = '\d\d\d-\d\d\d-\d\d\d\d'
quantifier_regex = r'(\d{3})-(\d{3})-(\d{4})'
found_match = re.search(regex_for_phone_number, phone_number)
quantifier_found_match = re.search(quantifier_regex, phone_number)
print(found_match.group())
print(quantifier_found_match.group(3))

#This will remove punctuation out of a given string
punc_sentence = "This is a sentence! It has punctuation. How can we remove it?"
regex_remove_punc = "[^!.? ]+"
match_remove_punc = re.findall(regex_remove_punc, punc_sentence)
clean = ' '.join(match_remove_punc)
print(punc_sentence)
print(match_remove_punc)
print(clean)

#How to find words that are hyphenated
hyphen_text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
regex_hyphen = r'[\w]+-[\w]+'
match_hyphen_words = re.findall(regex_hyphen, hyphen_text)
print(hyphen_text)
print(match_hyphen_words)

#This will allow for multiple options in searching
#If we have multiple options for matching, we can use parenthesis to list out these options.
multiple_text = 'Hello, would you like some catfish?'
multiple_texttwo = "Hello, would you like to take a catnap?"
multiple_textthree = "Hello, have you seen this caterpillar?"

regex_multiple = r'cat(fish|nap|claw)'

print(re.search(regex_multiple, multiple_text).group())
print(re.search(regex_multiple, multiple_texttwo).group())
print(re.search(regex_multiple, multiple_textthree))