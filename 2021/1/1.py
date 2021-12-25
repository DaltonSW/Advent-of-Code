def main():
    f = open('input.txt')
    num = int(f.readline())
    count = 0
    for line in f.readlines():
        check = int(line)
        if check > num:
            count += 1
        num = check
    print(count)
    f.close()

main()


