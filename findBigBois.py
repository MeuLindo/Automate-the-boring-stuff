#! python3

import os
from pathlib import Path
from time import sleep


for folderName, subFolders, filenames in os.walk('/'):
	print('Começando o scan...')
	# sleep(2)
	print(folderName)
	print(subFolders)
	print(filenames)
	for filename in filenames:
		filePath = Path(folderName) / filename
		print(filePath)
		print(filename)
		try:
			print(os.path.getsize(filePath))
		except:
			pass
		# sleep(0.5)


