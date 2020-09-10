def palindrome(word):
    rev_word= ""
    for m in range(1,len(word)+1):
        rev_word = rev_word + word[-m]
    if word == rev_word:
        return "Your word is palindrome"
    else:
        return"your word is not palindrome"
word = input("Please enter you word: ")
result = palindrome(word)
print(result)   
    