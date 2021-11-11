import os

src_dir = os.getcwd()
for count,name in enumerate(os.listdir('.')):
	if name.endswith('.jpg') or name.endswith('.jpeg'):
		os.rename(name, f'{count:05d}' + '.jpg')