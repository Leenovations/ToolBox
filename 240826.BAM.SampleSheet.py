#!/usr/bin/python3
import sys
import os

LIST = sys.argv[1:]

with open('BAMDatalist.txt', 'w') as note2:
	for data in LIST:
		note2.write(data + '\n')
		
with open('BAMSampleSheet.txt', 'w') as note1:
	for data in LIST:
		Name = data.split('/')[-1]
		Path = data
		Size = os.path.getsize(data)
		note1.write(Name + '\t' + Path + '\t' + Path + '\t' + str(Size) + '\n')
		
		with open(f'{Path}/BAMSampleSheet.txt', 'w') as note2:
			Name = data.split('/')[-1]
			Path = data
			note2.write(Name + '\t' + Path + '\t' + Path + '\t' + str(Size) + '\n')