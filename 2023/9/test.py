x = 0

def foo():
    global x
    x += 1

def bar():
    x += 1

def main():
    foo()
    bar()

    print(x)

main()
print(x)