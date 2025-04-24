import random
import re


text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result

def memberOne(text):
    words = re.findall(r'\b\w+\b', text)
    vowels = set('aeiouAEIOU')
    count = sum(1 for word in words if any(char in vowels for char in word))
    return count
  
<<<<<<< Updated upstream
def memberOne():
    vowels = set("aeiouAEIOU")
    with open(text, "r", encoding="utf-8") as f:
        paragraph = f.read()
    words = paragraph.split()
    count = sum(1 for word in words if any(char in vowels for char in word))
    return count
=======
def memberTwo(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result
shift_value = 1
>>>>>>> Stashed changes
  
def memberThree(text):
    lines = text.split('\n')  # Split by lines
    reversed_lines = [line[::-1] for line in lines]
    return '\n'.join(reversed_lines)
  
def memberFour(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


if __name__ == "__main__":
    print(hammer_task_0())
    print('call memberOne() ', memberOne(text))
    print('call memberTwo() ', memberTwo(text, shift_value))
    print('call memberThree() ', memberThree(text))
    print('call memberFour() ', memberFour(text))
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob