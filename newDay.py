import sys, os, traceback, shutil

try:
    year = sys.argv[1]
    day = sys.argv[2]
    path = './{}/{}'.format(year, day)
    os.makedirs(path)
    shutil.copy('./basefile.py', '{}/1.py'.format(path))

except:
    print("Error!")
    print(traceback.format_exc())
