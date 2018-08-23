# wsu library photobooth file copier

import sys
import os

# get folders
INPUT_FOLDER = sys.argv[1].replace(' ','\ ')
OUTPUT_FOLDER = sys.argv[2].replace(' ','\ ')

# run fswatch
print("Starting photobooth file copier from %s --> %s" % (INPUT_FOLDER, OUTPUT_FOLDER))
os.system('fswatch -0 %s | xargs -0 -n1 -I {} cp {$1} %s' % (INPUT_FOLDER, OUTPUT_FOLDER))
