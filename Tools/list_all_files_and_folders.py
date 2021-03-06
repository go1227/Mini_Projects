__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "2/29/2020"
__python_version__ = "3"
__notes__ = "PEP8 compliant"

import os

start = '/'

try:
	with os.scandir(start) as entries:
		for entry in entries:
			print(entry.name)
except Exception as e:
	print(f'Failed to read the folder {start}: '+ str(e))
	# raise