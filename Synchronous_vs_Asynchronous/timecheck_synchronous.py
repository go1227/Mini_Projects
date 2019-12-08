__author__ = "Gil Ortiz"
__version = "1.0"
__date_last_modification__ = "12/7/2019"
__notes__ = ''' timecheck_synchronous.py - routine executed in standard synchronous mode
				when executed, get_data() will be called synchronously 6x'''

import time
import random
import string

start = time.time()


def get_data():
	# random_num = random.randint(1,100)
	letters_and_numbers = string.ascii_uppercase + string.ascii_lowercase + ''.join([str(i) for i in range(10)])
	random_password = ''.join(random.choice(letters_and_numbers) for i in range(10))
	print("Random generated password is %s ------ %.2f seconds" % (random_password, time.time() - start))
	time.sleep(2)  # this simulates "processing time" in the get_data() function.


def main():
	# get_data() will be called 6 times in sequence (traditional synchronous programming)
	get_data()
	get_data()
	get_data()
	get_data()
	get_data()
	get_data()


if __name__ == '__main__':
	main()