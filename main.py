# coding: utf-8

import ui
import model
import console
from datetime import datetime, timedelta

@ui.in_background
def send_action(sender):
	global main_view
	weight = main_view['textfield_weight'].text
	try:
		model.register_weight(float(weight))
		weight_changed_action(sender)
	except BaseException as e:
		console.hud_alert(str(e), 'error')
	else:	
		console.hud_alert('Done!', 'success')
		
def weight_changed_action(sender):
	global main_view
	weight_text = main_view['textfield_weight'].text
	height_text = main_view['textfield_height'].text
	try:
		weight = float(weight_text)
		height = float(height_text)
		main_view['textfield_imc'].text = '{:.1f}'.format(model.compute_imc(weight, height))
	except:
		pass

def switch_test_mode_action(sender):
	global main_view
	model.test_mode = main_view['switch_test_mode'].value
	
model.test_mode = False  

main_view = ui.load_view('main')
height = model.get_height()

main_view['textfield_height'].text = str(height)
main_view['textfield_height'].enabled = False 
main_view['textfield_weight'].action = weight_changed_action
main_view['switch_test_mode'].value = model.test_mode
main_view['textfield_ideal_weight'].text = '{:.1f}'.format(model.ideal_weight(height))
main_view['textfield_height'].enabled = False 

main_view['trend_15_days'].text = '{:.1f} Kg'.format(model.estimate_weight(datetime.now() - timedelta(weeks=2)))

main_view['trend_30_days'].text = '{:.1f} Kg'.format(model.estimate_weight(datetime.now() - timedelta(weeks=4)))

#model.generate_plot()
import StringIO
from PIL import Image
pilimg = Image.open('plot.png')
strio = StringIO.StringIO()
pilimg.save(strio, pilimg.format)
data = strio.getvalue()
strio.close()
main_view['plot'].image = ui.Image.from_data(data)
main_view.present()
