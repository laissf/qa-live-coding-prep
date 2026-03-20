#Verify if a word is a palindromo

def is_palindrome(word):
    wordReverse = ""
    for n in range(len(word)):
        position = len(word) - 1 - n
        wordReverse += word[position]

    return  word == wordReverse