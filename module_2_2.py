first, second, third = int(input()), int(input()), int(input())
if first == second or first == third:
    if second == third:
        print(3)
    else:
        print(2)
elif second == third:
    print(2)
else:
    print(0)