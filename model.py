from datetime import datetime

test_mode = False 

def register_weight(value):
	"""register weight. value should be a float"""
	logline = str(datetime.now()) + ',' + str(float(value)) + '\n'
	
	if test_mode:
		print logline
	else:
		f = open('data.txt', 'a')
		f.write(logline)
		f.close()
		
def compute_imc(weight, height):
	return weight / (height * height)
	
def ideal_weight(height):
	return 24.9 * height * height

def get_height(): return 1.72
