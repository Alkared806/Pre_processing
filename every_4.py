import os
import shutil
src_dir = os.getcwd()
dst_dir = src_dir + '/done'

for name in os.listdir('.'):
	if name.endswith('.jpg'):
		if int(name.split('.')[0][2:]) % 4 == 0:
			shutil.copyfile(src_dir +'/' +name, dst_dir+ '/' + name)