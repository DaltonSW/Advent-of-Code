import sys, os, traceback, shutil

try:
    day = sys.argv[1]
    path = './{}'.format(day)
    os.mkdir(path)
    shutil.copy('./basefile.py', '{}/1.py'.format(path))

except:
    print("Error!")
    print(traceback.format_exc())