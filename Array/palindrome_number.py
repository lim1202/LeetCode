# Determine whether an integer is a palindrome. Do this without extra space.


def is_palindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True

    tmp = x
    y = 0
    
    while x != 0:
        y = y * 10 + x % 10
        x = x // 10
    
    if y == tmp:
        return True
    else
        return False


if __name__ == '__main__':
    print('121 is palindrome?', is_palindrome(121))
    print('122 is palindrome?', is_palindrome(122))
