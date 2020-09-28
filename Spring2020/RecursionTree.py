# first recursion

def foo1(n):
    if n > 1:
        print('hi ' + 'hi ' + 'hi')
        foo1(n/4)
        foo1(n/4)
        foo1(n/4)
    else:
        return

def relation1(n):
    if n <= 1:
        return 0
    elif n <= 4:
        return 3
    return 3 * relation1(n/4) + 3




# second recursion

def foo2(n):
    if n > 1:
        for i in range(1, int(n) + 1):
            print('hi ' + 'hi')
        foo2(n/4)
        foo2(n/4)
        foo2(n/4)
    else:
        return

def relation2(n):
    if n <= 1:
        return 0
    else:
        return 3 * relation2(n/4) + 2 * int(n)


def main():
    n = 4
    foo1(n)
    print(relation1(n))
    foo2(n)
    print(relation2(n))

main()
