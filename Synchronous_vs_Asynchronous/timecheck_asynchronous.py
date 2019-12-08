__author__ = "Gil Ortiz"
__version = "1.0"
__date_last_modification__ = "12/7/2019"
__notes__ = ''' timecheck_asynchronous.py - routine executed in an asynchronous fashion.
				when executed, get_data() will be called asynchronously 6x - the execution time printed shows that they are all executed about the same time.'''

import asyncio
import time
import random
import string

start = time.time()


async def get_data():
	while True:
		await asyncio.sleep(2)  # this simulates "processing time" in the get_data() function.
		letters_and_numbers = string.ascii_uppercase + string.ascii_lowercase + ''.join([str(i) for i in range(10)])
		random_password = ''.join(random.choice(letters_and_numbers) for i in range(10))
		print("Random number is %s ------ %.2f seconds" % (random_password, time.time()-start))

loop = asyncio.get_event_loop()

try:
	# each loop will call "get_data()" 6 times
	asyncio.ensure_future(get_data())
	asyncio.ensure_future(get_data())
	asyncio.ensure_future(get_data())
	asyncio.ensure_future(get_data())
	asyncio.ensure_future(get_data())
	asyncio.ensure_future(get_data())
	loop.run_forever()
except KeyboardInterrupt:
	pass
finally:
	print("Closing Loop")
	loop.close()
