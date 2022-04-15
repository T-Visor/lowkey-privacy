from glob import glob
import sys
import subprocess

subdirectories = glob('imgs/*/', recursive = True)

print('===FOLDERS FOUND===')
for folder in subdirectories:
    print(folder)
print('===================\n')

for folder in subdirectories:
    print('Processing folder:', folder)
    subprocess.call([sys.executable, 'attack_dir_warp', '--dir', folder])
