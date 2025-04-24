import random
 
text = './news.txt'
 
def hammer_task_0():
    '''example function'''
    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
 
 
def memberOne():
    # Task-1: Count words containing at least one vowel
    vowels = set("aeiouAEIOU")
    with open(text, "r", encoding="utf-8") as f:
        paragraph = f.read()
    words = paragraph.split()
    count = sum(1 for word in words if any(char in vowels for char in word))
    return count
 
 
def memberTwo(shift=1):
    # Task-2: Encode the paragraph by shifting each character by a variable value
    with open(text, "r", encoding="utf-8") as f:
        paragraph = f.read()
    encoded = ''
    for char in paragraph:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            encoded += char
    return encoded
 
 
def memberThree():
    # Task-3: Reverse the entire paragraph line by line
    with open(text, "r", encoding="utf-8") as f:
        lines = f.readlines()
    reversed_lines = [line.strip()[::-1] for line in lines]
    return "\n".join(reversed_lines)
 
 
def memberFour():
    # Task-4: Reverse the order of characters of each word
    with open(text, "r", encoding="utf-8") as f:
        paragraph = f.read()
    words = paragraph.split()
    reversed_words = [''.join(reversed(word)) for word in words]
    return ' '.join(reversed_words)
 
 
if __name__ == "__main__":
    print("Random member:", hammer_task_0())
    print("Words with vowels:", memberOne())
    print("Encoded paragraph (shift=1):\n", memberTwo())
    print("Reversed lines:\n", memberThree())
    print("Reversed characters of each word:\n", memberFour())