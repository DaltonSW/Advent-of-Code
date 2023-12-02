import os
import shutil
import sys
import traceback

try:
    year = sys.argv[1]
    day = sys.argv[2]
    path = './{}/{}'.format(year, day)
    os.makedirs(path)
    shutil.copy('./basefile.py', '{}/1.py'.format(path))
    shutil.copy('./basefile.py', '{}/2.py'.format(path))
    os.chdir(path)

except:
    print("Error!")
    print(traceback.format_exc())
