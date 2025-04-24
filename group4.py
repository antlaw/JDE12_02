import random

text = './news.txt'
f = open(text, "r")
content = f.read()
print('original content:')
print(content)
print('')

def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne(content):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = content.split()
    count = 0
    
    for word in words:
        if any(char.lower() in vowels for char in word):
            count += 1
    
    return count
  
def memberTwo(content, shift=1):
    encoded = []
    for char in content:
        if char.isalpha():
            # Shift characters while maintaining case
            base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - base + shift) % 26 + base)
            encoded.append(encoded_char)
        else:
            # Keep non-alphabetic characters unchanged
            encoded.append(char)
    return ''.join(encoded)
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    # print(hammer_task_0())
    print(f'Words with vowels: {memberOne(content)}')
    print(f'Encoded text: {memberTwo(content)}')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
