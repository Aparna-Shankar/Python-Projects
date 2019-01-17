import os
import glob

os.chdir('/Users/aparnashankar/Documents/Furniture')


# f1 = f_name.split('-')

# Sort the file names by created time
f = sorted(filter(os.path.isfile, os.listdir(os.curdir)), key=os.path.getctime)
f_num = 1
for file in f:
    f_name, f_extn = os.path.splitext(file)
    # Form the new file name
    new_name = f'{str(f_num).zfill(2)}_{f_name}{f_extn}'
    f_num += 1
    # Rename the file
    os.rename(file, new_name)
