import random

text = '/Users/vickiliu/Documents/GitHub/JDE12_02/news.txt'
f = open(text, "r")
paragraph=f.read()


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def count_words_with_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = text.split()  # Split into words
    count = 0
    
    for word in words:
        # Check if any vowel is in the word (case-insensitive)
        if any(vowel in word.lower() for vowel in vowels):
            count += 1
    
    return count

# Call the function
total_words_with_vowels = count_words_with_vowels(paragraph)
print(f"Total words containing vowels: {total_words_with_vowels}")
pass
  
def memberTwo():
    pass
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
