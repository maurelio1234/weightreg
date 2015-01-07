from datetime import datetime, timedelta
from PIL import Image
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

def load_data():
	with open('data.txt') as f:
		ret = []
		for line in f:
			s = line.split(',')
			dt = datetime.strptime(s[0], "%Y-%m-%d %H:%M:%S.%f")
			weight = float(s[1])
			ret.append((dt,weight))
		return ret
			
def estimate_weight(date):
		last_date = None 
		current_date = None 
		
		last_weight = 0
		current_weight = 0
		
		for (dt,weight) in load_data():
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

def generate_plot():
	import matplotlib.pyplot as plt
	from matplotlib.dates import date2num
	
	data = load_data()
	plt.plot_date(x=[date2num(dt) for (dt,w) in data],
	              y=[w for (dt,w) in data],
	              xdate=True,
	              linestyle='-',
	              linewidth=2,
	              antialiased=True,
	              marker=None) # TODO: how to hide markers?
	# TODO: how to properly format and space dates?
	plt.show()
	plt.savefig('plot.png')
	return Image.open('plot.png')
#generate_plot()
