import time

def main():
    f = open('input.txt', 'r')

    # parsing code here

    f.close()

    # remaining code here


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
