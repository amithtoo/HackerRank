t = int(input())
while t:
    text = input()
    for i in range(len(text)):
        if i%2 == 0:
            print(text[i], end='')
    print(' ', end='')
    for i in range(len(text)):
        if i%2 != 0:
            print(text[i], end='')
    print()
    t -= 1
