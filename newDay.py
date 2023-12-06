import os
import shutil
import sys
import traceback
from datetime import date

if len(sys.argv) == 1:
    today = date.today()
    year = today.year
    day = today.day

else:
    try:
        year = sys.argv[1]
        day = sys.argv[2]
    except:
        print("Error!")
        print(traceback.format_exc())
        quit()

path = './{}/{}'.format(year, day)
os.makedirs(path)
shutil.copy('./basefile.py', '{}/1.py'.format(path))
shutil.copy('./basefile.py', '{}/2.py'.format(path))
os.chdir(path)


