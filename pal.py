def check_palindrome(string):
    half_len = len(string) // 2 #loop through half the string
    for i in range(half_len):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

user_input = input('what is your word? ')
print(check_palindrome(user_input))
