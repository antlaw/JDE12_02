import random

text = './news.txt'
with open(text, "r") as f:
    paragraph = f.read()

def hammer_task_0():
    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
 
 # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
def memberOne(text):
    vowels = set('aeiouAEIOU')
    words = text.split()
    vowel_count = sum(1 for word in words if any(char in vowels for char in word))
    return f"Words with vowels: {vowel_count}"


# Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz
def memberTwo(text, shift=1):
    encoded = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            encoded += char
    return encoded


# Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
def memberThree(text):
    lines = text.split('\n')
    reversed_lines = [line[::-1] for line in lines]
    return '\n'.join(reversed_lines)



# Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
def memberFour(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    result = []
    current_word = 0
    for char in text:
        if char.isspace() or char == '\n':
            result.append(char)
        else:
            result.append(reversed_words[current_word][0])
            reversed_words[current_word] = reversed_words[current_word][1:]
            if not reversed_words[current_word]:
                current_word += 1
    return ''.join(result)

if __name__ == "__main__":
    print(hammer_task_0())
    print('call memberOne():', memberOne(paragraph))
    print('call memberTwo():', memberTwo(paragraph))
    print('call memberThree():', memberThree(paragraph))
    print('call memberFour():', memberFour(paragraph))