'''
#연습
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else: return False

print(is_palindrome('hello'))
print(is_palindrome('level'))
'''
#심사
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))