# This is a test script for python shell
import time
import numpy as np
x=0
for i in range(1,11):
	x = np.sqrt(x+i**2)
	print('The new count is: ' + str(x))
	time.sleep(1)

