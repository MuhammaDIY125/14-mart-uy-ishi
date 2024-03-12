# 2-masala. TWO PARTS
# s = "Hi"
# s = "Hello"
s = input(">>> ")
n = len(s) // 2
s = s[-n:] + s[:-n]
print(s)