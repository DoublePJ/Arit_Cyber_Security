from palindrome import is_palindrome

def check_palindrom():

    user_input = input("Enter Text: ")
    is_palin = is_palindrome(user_input)
    print(f"Original Text: '{user_input}'")
    
    if is_palin:
        print("Is Palindrome")
    else:
        print("Is not Palindrome.")
        
if __name__ == "__main__":
    check_palindrom()