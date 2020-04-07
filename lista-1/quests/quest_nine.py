def is_palindrome(text):
    reverse_text = ''.join(reversed(text))

    if(text == reverse_text):
        return True
    else:
        return False

