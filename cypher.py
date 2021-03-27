#This program hides a null cypher within a give list.
#Uses the program load_dictionary to do so.

#Required
from random import randint
import string
import load_dictionary

# Message should use no punctuation or numbers
user_message = input("Input a message to cipher. The message should not contain punctuation or numbers\n")
user_message.translate(string.punctuation)
message = ''
for char in user_message:
    if char in string.ascii_letters:
        message += char
print(message, "\n")
message = "".join(message.split())

# open dictionary file
word_list = load_dictionary.loadFile('dictionary.txt')
i = 0
# build vocabulary word list with hidden message
vocab_list = []
for letter in message:
    size = randint(6, 10)
    for word in word_list:
        if len(word) == size and word[i].lower() == letter.lower()\
        and word not in vocab_list:
            vocab_list.append(word)
            i+=1
            if i > 4:
                i = 0
            break
        
if len(vocab_list) < len(message):
    print("Word List is too small. Try larger dictionary or shorter message!")
else:        
    print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")        
  

