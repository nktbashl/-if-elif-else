a = int(input())
b = int(input())
c = int(input())

if a != b != c:
    print(0)
if a == b == c:
    print(3)
elif a == c or a == b or b == c:
    print(2)

