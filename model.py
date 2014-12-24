from datetime import datetime, timedelta

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

def estimate_weight(date):
	with open('data.txt') as f:
		last_date = None 
		current_date = None 
		
		last_weight = 0
		current_weight = 0
		
		for line in f:
			s = line.split(',')
			dt = datetime.strptime(s[0], "%Y-%m-%d %H:%M:%S.%f")
			weight = float(s[1])
			
			last_date = current_date
			current_date = dt
			
			last_weight = current_weight
			current_weight = weight
			
			if not last_date: last_date = current_date
			if not last_weight: last_weight = current_weight
			
			if date < current_date:
				return current_weight
				
			if date > last_date and date < current_date:
				avg_weight = (last_weight+current_weight)/2
				return avg_weight
				
	return None 
	
# usage			
#print 'one week: ', estimate_weight(datetime.now() - timedelta(weeks=2))
#print 'one month: ', estimate_weight(datetime.now() - timedelta(weeks=3))
