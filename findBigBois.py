#! python3

import os
from pathlib import Path
from time import sleep

umMega = 1e+6
umGiga = 1e+9

BIGBOIS = []
BIGFOLDERS = []

folderAlvo = input('Qual pasta você quer escanear?\n')

for folderName, subFolders, filenames in os.walk(folderAlvo):
	print('Começando o scan em: ', folderName)

	for filename in filenames:
		filePath = Path(folderName) / filename
		totalFolderSize = 0
	
		try:
			totalFolderSize += os.path.getsize(filePath)
			if (os.path.getsize(filePath) > umGiga):
				BIGBOIS.push(filePath,filename,os.path.getsize(filePath))
			if totalFolderSize > umGiga:
				BIGFOLDERS.push(folderName)
		except:
			pass

print(BIGBOIS)
print(BIGFOLDERS)