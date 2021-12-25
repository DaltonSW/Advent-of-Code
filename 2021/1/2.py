def main():
    f = open('./input.txt', 'r')
    count = 0 
    prev = 999999999
    lines = f.readlines()
    for index in range(len(lines)):
        try:
            total = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
            if total > prev:
                count += 1
            prev = total
        except(IndexError):
            break
    print(count)
    f.close()

main()


