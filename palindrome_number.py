def isPalindrome( x: int):
    k = str(x)
    z = k[::-1]
    if k == z:
        return True
    else:
        return False
x = int(input())
result = isPalindrome(x)
print(result)


