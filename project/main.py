# made by: Raghav Awasthi

# basic pygame modules
import pygame
from pygame.locals import *
import sys
import pygame_gui
# for currency conversion
import requests
# file not included on github - refer to README
import APIs
# for calendar conversion
from jdcal import gcal2jd, jd2gcal, jd2jcal, jcal2jd

# all colours
black = (0, 0, 0)
light_blue = pygame.Color('lightskyblue3')
dark_blue = pygame.Color('gray15')
red = (202, 46, 23)
gray = (56, 77, 95)
dark_green = (8, 76, 8)
light_green = (8, 134, 8)
dark_orange = (108, 63, 14)
light_orange = (161, 91, 14)
yellow = (202, 142, 23)
white = (197, 203, 216)

# used to identify where to go when p pressed
curr_screen = None
prev_screen = None

# pygame initialization
pygame.init()
clock = pygame.time.Clock()

# set window + dock icon
display_size = (800, 800)
display = pygame.display.set_mode(display_size, 0, 32)
manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
dock_icon = pygame.image.load('images/converter_icon.png')
pygame.display.set_icon(dock_icon)

# set background
display.fill(gray)

# creates surface with same size as window - draw/create shapes on it
background = pygame.Surface(display_size)
display.blit(background, (0, 0))

pygame.display.update()

# all functions + classes
# pound and kg
def lb_to_kg(val):
	return val / 2.204622622

def kg_to_lb(val):
	return val * 2.204622622

# pound and stone
def lb_to_st(val):
	return val * 0.071429

def st_to_lb(val):
	return val / 0.071429

# kg and stone
def kg_to_st(val):
	return lb_to_st(kg_to_lb(val))

def st_to_kg(val):
	return lb_to_kg(st_to_lb(val))

# inch and centimetre
def inch_to_cm(val):
	return val * 2.54

def cm_to_inch(val):
	return val / 2.54

# metre and yard
def m_to_yd(val):
	return val / 0.9144

def yd_to_m(val):
	return val * 0.9144

# mile and kilometre + miles/hour and kilometres/hour
def mile_to_km(val):
	return val * 1.609344

def km_to_mile(val):
	return val / 1.609344

# centimetres, metres and kilometres
def cm_to_m(val):
	return val / 100

def m_to_km(val):
	return val / 1000

def cm_to_km(val):
	return m_to_km(cm_to_m(val))

def m_to_cm(val):
	return val * 100

def km_to_m(val):
	return val * 1000

def km_to_cm(val):
	return m_to_cm(km_to_m(val))

# miles/hour and knots
def mph_to_kts(val):
	return val / 1.15078

def kts_to_mph(val):
	return val * 1.15078

# kilometres/hour and knots
def kmph_to_kts(val):
	return mph_to_kts(km_to_mile(val))

def kts_to_kmph(val):
	return mile_to_km(kts_to_mph(val))

# fahrenheit and celsius
def f_to_c(val):
	return ((val - 32) * 5) / 9

def c_to_f(val):
	return (val * 1.8) + 32

# celsius and kelvin
def c_to_k(val):
	return val + 273.15

def k_to_c(val):
	return val - 273.15

# fahrenheit and kelvin
def f_to_k(val):
	return c_to_k(f_to_c(val))

def k_to_f(val):
	return c_to_f(k_to_c(val))

# gregorian and julian
def gregorian_to_julian(day, month, year):
	final_tuple = jd2jcal(*gcal2jd(year, month, day))
	# as day, month, year
	return final_tuple[2], final_tuple[1], final_tuple[0]

def julian_to_gregorian(day, month, year):
	final_tuple = jd2gcal(*jcal2jd(year, month, day))
	# as day, month, year
	return final_tuple[2], final_tuple[1], final_tuple[0]

# parent-class
class main_units:
	# val - value to convert, unit_1 - convert from, unit_2 - convert to
	def __init__(self, val, unit_1, unit_2):
		self.val = val
		self.unit_1 = unit_1
		self.unit_2 = unit_2

# 5 sub-classes of parent-class (main_units)
# take options and choose conversion function, convert and then return
class mass(main_units):
	def convert(self):

		if self.unit_1 == 'lb':
			if self.unit_2 == 'kg':
				return lb_to_kg(self.val)

			elif self.unit_2 == 'st':
				return lb_to_st(self.val)

			else:
				return self.val

		elif self.unit_1 == 'kg':
			if self.unit_2 == 'lb':
				return kg_to_lb(self.val)

			elif self.unit_2 == 'st':
				return kg_to_st(self.val)

			else:
				return self.val

		else:
			if self.unit_2 == 'lb':
				return st_to_lb(self.val)

			elif self.unit_2 == 'kg':
				return st_to_kg(self.val)

			else:
				return self.val

class length(main_units):
	def convert(self):

		if self.unit_1 == 'cm':
			if self.unit_2 == 'm':
				return cm_to_m(self.val)

			elif self.unit_2 == 'km':
				return cm_to_km(self.val)

			elif self.unit_2 == 'inch':
				return cm_to_inch(self.val)

			elif self.unit_2 == 'yd':
				return m_to_yd(cm_to_m(self.val))

			elif self.unit_2 == 'mile':
				return km_to_mile(cm_to_km(self.val))

			else:
				return self.val

		elif self.unit_1 == 'm':
			if self.unit_2 == 'cm':
				return m_to_cm(self.val)

			elif self.unit_2 == 'km':
				return m_to_km(self.val)

			elif self.unit_2 == 'inch':
				return cm_to_inch(m_to_cm(self.val))

			elif self.unit_2 == 'yd':
				return m_to_yd(self.val)

			elif self.unit_2 == 'mile':
				return km_to_mile(m_to_km(self.val))

			else:
				return self.val

		elif self.unit_1 == 'km':
			if self.unit_2 == 'cm':
				return km_to_cm(self.val)

			elif self.unit_2 == 'm':
				return km_to_m(self.val)

			elif self.unit_2 == 'inch':
				return cm_to_inch(km_to_cm(self.val))

			elif self.unit_2 == 'yd':
				return m_to_yd(km_to_m(self.val))

			elif self.unit_2 == 'mile':
				return km_to_mile(self.val)

			else:
				return self.val

		elif self.unit_1 == 'inch':
			if self.unit_2 == 'cm':
				return inch_to_cm(self.val)

			elif self.unit_2 == 'm':
				return cm_to_m(inch_to_cm(self.val))

			elif self.unit_2 == 'km':
				return cm_to_km(inch_to_cm(self.val))

			elif self.unit_2 == 'yd':
				return m_to_yd(cm_to_m(inch_to_cm(self.val)))

			elif self.unit_2 == 'mile':
				return km_to_mile(cm_to_km(inch_to_cm(self.val)))

			else:
				return self.val

		elif self.unit_1 == 'yd':
			if self.unit_2 == 'cm':
				return m_to_cm(yd_to_m(self.val))

			elif self.unit_2 == 'm':
				return yd_to_m(self.val)

			elif self.unit_2 == 'km':
				return m_to_km(yd_to_m(self.val))

			elif self.unit_2 == 'inch':
				return cm_to_inch(m_to_cm(yd_to_m(self.val)))

			elif self.unit_2 == 'mile':
				return km_to_mile(m_to_km(yd_to_m(self.val)))

			else:
				return self.val

		elif self.unit_1 == 'mile':
			if self.unit_2 == 'cm':
				return km_to_cm(mile_to_km(self.val))

			elif self.unit_2 == 'm':
				return km_to_m(mile_to_km(self.val))

			elif self.unit_2 == 'km':
				return mile_to_km(self.val)

			elif self.unit_2 == 'inch':
				return cm_to_inch(km_to_cm(mile_to_km(self.val)))

			elif self.unit_2 == 'yd':
				return m_to_yd(km_to_m(mile_to_km(self.val)))

			else:
				return self.val

		else:
			return self.val

class speed(main_units):
	def convert(self):

		if self.unit_1 == 'mph':
			if self.unit_2 == 'kmph':
				return mile_to_km(self.val)

			elif self.unit_2 == 'kts':
				return mph_to_kts(self.val)

			else:
				return self.val

		elif self.unit_1 == 'kmph':
			if self.unit_2 == 'mph':
				return km_to_mile(self.val)

			elif self.unit_2 == 'kts':
				return kmph_to_kts(self.val)

			else:
				return self.val

		elif self.unit_1 == 'kts':
			if self.unit_2 == 'mph':
				return kts_to_mph(self.val)

			elif self.unit_2 == 'kmph':
				return kts_to_kmph(self.val)

			else:
				return self.val

		else:
			return self.val

class temperature(main_units):
	def convert(self):

		if self.unit_1 == 'c':
			if self.unit_2 == 'f':
				return c_to_f(self.val)

			elif self.unit_2 == 'k':
				return c_to_k(self.val)

			else:
				return self.val

		elif self.unit_1 == 'f':
			if self.unit_2 == 'c':
				return f_to_c(self.val)

			elif self.unit_2 == 'k':
				return f_to_k(self.val)

			else:
				return self.val

		elif self.unit_1 == 'k':
			if self.unit_2 == 'c':
				return k_to_c(self.val)

			elif self.unit_2 == 'f':
				return k_to_f(self.val)

			else:
				return self.val

		else:
			return self.val

class currency(main_units):
	# empty dict to store the conversion rates
	rates = {}

	def __init__(self, url):
		data = requests.get(url).json()

		# Extracting only the rates from the json data
		self.rates = data["rates"]

	# function to do a simple cross multiplication between
	# the amount and the conversion rates
	def convert(self, amount, from_currency, to_currency):
		if from_currency != 'EUR':
			amount = amount / self.rates[from_currency.upper()]

		# limiting the precision to 2 decimal places
		amount = round(amount * self.rates[to_currency.upper()], 2)
		return amount

class calendar():
	def __init__(self, unit_1, unit_2, dates):
		self.unit_1 = unit_1
		self.unit_2 = unit_2
		self.dates = dates

	def convert(self):

		if self.unit_1 == 'gregorian':
			if self.unit_2 == 'julian':
				return gregorian_to_julian(self.dates[0], self.dates[1], self.dates[2])
			else:
				return self.dates[0], self.dates[1], self.dates[2]

		elif self.unit_1 == 'julian':
			if self.unit_2 == 'gregorian':
				return julian_to_gregorian(self.dates[0], self.dates[1], self.dates[2])
			else:
				return self.dates[0], self.dates[1], self.dates[2]

		else:
			return self.dates[0], self.dates[1], self.dates[2]

# main pygame code
# quickly create objects (rects)
def text_objects(text, font, colour):

	text_surf = font.render(text, True, colour)
	return text_surf, text_surf.get_rect()

# go back to previous window/screen when p pressed on keyboard
def return_to_prev_screen(prev_screen, curr_screen):

	if prev_screen is None:
		return 'intro', prev_screen, curr_screen

	elif prev_screen == 'instructions':
		return 'instructions', prev_screen, curr_screen

	elif prev_screen == 'intro':
		return 'intro', prev_screen, curr_screen

	elif prev_screen == 'mass':
		return 'mass', prev_screen, curr_screen

	elif prev_screen == 'length':
		return 'length', prev_screen, curr_screen

	elif prev_screen == 'speed':
		return 'speed', prev_screen, curr_screen

	elif prev_screen == 'temp':
		return 'temp', prev_screen, curr_screen

	elif prev_screen == 'currency':
		return 'currency', prev_screen, curr_screen

	elif prev_screen == 'cal':
		return 'cal', prev_screen, curr_screen

	else:
		return 'intro', prev_screen, curr_screen

# run window/screen based on user's choices
def screen_to_run(wdw, prev_screen, curr_screen):

	if wdw is False:
		pygame.quit()
		quit()

	elif wdw == 'intro':
		return introduction(prev_screen, curr_screen)

	elif wdw == 'instructions':
		return instructions(prev_screen, curr_screen)

	elif wdw == 'mass':
		return mass_wdw(prev_screen, curr_screen)

	elif wdw == 'length':
		return length_wdw(prev_screen, curr_screen)

	elif wdw == 'speed':
		return speed_wdw(prev_screen, curr_screen)

	elif wdw == 'temp':
		return temp_wdw(prev_screen, curr_screen)

	elif wdw == 'currency':
		return currency_wdw(prev_screen, curr_screen)

	elif wdw == 'cal':
		return cal_wdw(prev_screen, curr_screen)

	elif wdw == 'return_to_prev_screen':
		return return_to_prev_screen(prev_screen, curr_screen)

	else:
		return introduction(prev_screen, curr_screen)

	return wdw, prev_screen, curr_screen

# opening screen with all main buttons (conversions + instructions)
def introduction(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'intro'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Converters')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

	display.fill(gray)

	# instructions button under CONVERTERS title
	instructions_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((296, 175), (200, 100)),
	text = 'Instructions', manager = manager, object_id = '#instructions')

	# 6 main conversion buttons across middle, UIButton = styled
	mass_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((5, 300), (260, 200)),
	text = 'Mass', manager = manager, object_id = '#6_conversions')

	length_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((270, 300), (260, 200)),
	text = 'Length', manager = manager, object_id = '#6_conversions')

	speed_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((535, 300), (260, 200)),
	text = 'Speed', manager = manager, object_id = '#6_conversions')

	temp_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((5, 505), (260, 200)),
	text = 'Temp', manager = manager, object_id = '#6_conversions')

	currency_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((270, 505), (260, 200)),
	text = 'Currency', manager = manager, object_id = '#6_conversions')

	cal_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((535, 505), (260, 200)),
	text = 'Calendar', manager = manager, object_id = '#6_conversions')

	# title CONVERTERS at top of the screen
	title_text_font = pygame.font.Font('fonts/Montserrat-Bold.ttf', 105)
	text_surf, text_rect = text_objects('CONVERTERS', title_text_font, black)
	text_rect.center = ((display_size[0] / 2), (display_size[1] / 8))
	display.blit(text_surf, text_rect)

	while True:

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		for event in pygame.event.get():

			# red x on top left of every window = quit
			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.KEYDOWN:
				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					# instructions(prev_screen, curr_screen)
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					if event.ui_element == instructions_btn:
						return 'instructions', prev_screen, curr_screen

					if event.ui_element == mass_btn:
						return 'mass', prev_screen, curr_screen

					if event.ui_element == length_btn:
						return 'length', prev_screen, curr_screen

					if event.ui_element == speed_btn:
						return 'speed', prev_screen, curr_screen

					if event.ui_element == temp_btn:
						return 'temp', prev_screen, curr_screen

					if event.ui_element == currency_btn:
						return 'currency', prev_screen, curr_screen

					if event.ui_element == cal_btn:
						return 'cal', prev_screen, curr_screen

			manager.process_events(event)
		manager.update(time_delta)

		manager.draw_ui(display)
		pygame.display.flip()

# screen with instruction
def instructions(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'instructions'

	# set window + clear screen
	display_size = (800, 630)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Instructions')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

	display.fill(dark_green)

	while True:

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
		manager.update(time_delta)

		# instructions' text
		text_line_font = pygame.font.Font('fonts/Montserrat-Regular.ttf', 25)
		text_line_0 = text_line_font.render('Controls:', 1, yellow)
		text_line_1 = text_line_font.render('- To quit, either click the red '\
		+ 'button at the top left, or press', 1, white)
		text_line_2 = text_line_font.render('esc on the keyboard.', 1, white)
		text_line_3 = text_line_font.render('- To go back to the previous '\
		+ 'page you were on, press p on the ', 1, white)
		text_line_4 = text_line_font.render('keyboard.', 1, white)
		text_line_5 = text_line_font.render('- To open up this page again, '\
		+ 'press i on the keyboard.', 1, white)
		text_line_6 = text_line_font.render('- To go back to the main page, '\
		+ 'press m on the keyboard.', 1, white)
		text_line_7 = text_line_font.render('- You can click on any buttons '\
		+ '- buttons always light up when ', 1, white)
		text_line_8 = text_line_font.render('they are hovered over.', 1, white)
		text_line_9 = text_line_font.render('What to do:', 1, yellow)
		text_line_10 = text_line_font.render('- First, you must open a page '\
		+ 'for one of the conversions after ', 1, white)
		text_line_11 = text_line_font.render('clicking p to go back to the '\
		+ 'main home screen.', 1, white)
		text_line_12 = text_line_font.render('- Then, you must click on the '\
		+ 'dropdown menu on the left side.', 1, white)
		text_line_13 = text_line_font.render('- After selecting one of the '\
		+ 'units, you must then select a unit ', 1, white)
		text_line_14 = text_line_font.render('from the dropdown menu on '\
		+ 'the right side.', 1, white)
		text_line_15 = text_line_font.render('- You must then enter the '\
		+ 'number that needs to be converted ', 1, white)
		text_line_16 = text_line_font.render('from the dropdown menu on the '\
		+ 'left in the bar on the left.', 1, white)
		text_line_17 = text_line_font.render('- After clicking the convert '\
		+ 'button, the converted value will ', 1, white)
		text_line_18 = text_line_font.render('appear on the right.', 1, white)
		text_line_19 = text_line_font.render('REMEMBER:', 1, red)
		text_line_20 = text_line_font.render('You MUST choose the value to '\
		+ 'convert FROM on the LEFT!', 1, white)

		# put instructions on the screen
		display.blit(text_line_0, (5, (27 * 0)))
		display.blit(text_line_1, (5, (27 * 1)))
		display.blit(text_line_2, (5, (27 * 2)))
		display.blit(text_line_3, (5, (27 * 3)))
		display.blit(text_line_4, (5, (27 * 4)))
		display.blit(text_line_5, (5, (27 * 5)))
		display.blit(text_line_6, (5, (27 * 6)))
		display.blit(text_line_7, (5, (27 * 7)))
		display.blit(text_line_8, (5, (27 * 8)))
		display.blit(text_line_9, (5, (27 * 10)))
		display.blit(text_line_10, (5, (27 * 11)))
		display.blit(text_line_11, (5, (27 * 12)))
		display.blit(text_line_12, (5, (27 * 13)))
		display.blit(text_line_13, (5, (27 * 14)))
		display.blit(text_line_14, (5, (27 * 15)))
		display.blit(text_line_15, (5, (27 * 16)))
		display.blit(text_line_16, (5, (27 * 17)))
		display.blit(text_line_17, (5, (27 * 18)))
		display.blit(text_line_18, (5, (27 * 19)))
		display.blit(text_line_19, (5, (27 * 21)))
		display.blit(text_line_20, (5, (27 * 22)))

		manager.draw_ui(display)
		pygame.display.flip()

# mass conversion window / screen
def mass_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'mass'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Mass')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
	manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
	display.fill(dark_orange)

	user_text = ''
	# input space for user to enter numbers to be converted
	inp_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((50, 250), (250, 50)),
	manager = manager, object_id = '#input_boxes')

	comp_text = ''
	# output space where converted number is shown
	out_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((480, 250), (250, 50)),
	manager = manager, object_id = '#output_boxes')

	# conversion from
	curr_opt_1 = 'kg'
	opt_1_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['kilograms', 'pounds', 'stones'], starting_option = \
	'kilograms', relative_rect = pygame.Rect((50, 325), (270, 75)),
	manager = manager_dd)

	# conversion to
	curr_opt_2 = 'lb'
	opt_2_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['kilograms', 'pounds', 'stones'], starting_option = \
	'pounds', relative_rect = pygame.Rect((480, 325), (270, 75)),
	manager = manager_dd)

	# convert button clicked in order to conver
	convert_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((325, 150), (130, 60)),
	text = 'Convert', manager = manager, object_id = '#convert')

	inp_box.set_allowed_characters(
	['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
	out_box.set_allowed_characters([])

	while True:

		# get curr_opt_1 in abbreviated for to use for conversion
		if opt_1_dd.selected_option == 'kilograms':
			curr_opt_1 = 'kg'
		elif opt_1_dd.selected_option == 'pounds':
			curr_opt_1 = 'lb'
		elif opt_1_dd.selected_option == 'stones':
			curr_opt_1 = 'st'
		else:
			pass

		# get curr_opt_2 in abbreviated for to use for conversion
		if opt_2_dd.selected_option == 'kilograms':
			curr_opt_2 = 'kg'
		elif opt_2_dd.selected_option == 'pounds':
			curr_opt_2 = 'lb'
		elif opt_2_dd.selected_option == 'stones':
			curr_opt_2 = 'st'
		else:
			pass

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					# convert and display
					if event.ui_element == convert_btn:

						# clear output
						out_box.set_text('')

						user_text = inp_box.get_text()

						# initialize
						try:
							converter = mass(float(user_text), curr_opt_1, curr_opt_2)
						except ValueError:
							user_text = '0'
							converter = mass(float(user_text), curr_opt_1, curr_opt_2)

						comp_text = str(round(converter.convert(), 5))

						# allow to show text
						out_box.set_allowed_characters(
						['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
						# put final conversion in output
						out_box.set_text(comp_text)
						# make output uneditable
						out_box.set_allowed_characters([])

					if event.ui_element == inp_box:
						user_text = inp_box.get_text()

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
			manager_dd.process_events(event)
		manager.update(time_delta)
		manager_dd.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		manager.draw_ui(display)
		manager_dd.draw_ui(display)
		pygame.display.flip()

# length conversion window / screen
def length_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'length'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Length')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
	manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
	display.fill(dark_orange)

	user_text = ''
	# input space for user to enter numbers to be converted
	inp_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((50, 250), (250, 50)),
	manager = manager, object_id = '#input_boxes')

	comp_text = ''
	# output space where converted number is shown
	out_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((480, 250), (250, 50)),
	manager = manager, object_id = '#output_boxes')

	# conversion from
	curr_opt_1 = 'cm'
	opt_1_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['centimetres', 'metres', 'kilometres', 'inches', 'yards', \
	'miles'], starting_option = 'centimetres', relative_rect = \
	pygame.Rect((50, 325), (270, 75)), manager = manager_dd)

	# conversion to
	curr_opt_2 = 'm'
	opt_2_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['centimetres', 'metres', 'kilometres', 'inches', 'yards', \
	'miles'], starting_option = 'centimetres', relative_rect = \
	pygame.Rect((480, 325), (270, 75)), manager = manager_dd)

	# convert button clicked in order to conver
	convert_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((325, 150), (130, 60)),
	text = 'Convert', manager = manager, object_id = '#convert')

	inp_box.set_allowed_characters(
	['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
	out_box.set_allowed_characters([])

	while True:

		# get curr_opt_1 in abbreviated for to use for conversion
		if opt_1_dd.selected_option == 'centimetres':
			curr_opt_1 = 'cm'
		elif opt_1_dd.selected_option == 'metres':
			curr_opt_1 = 'm'
		elif opt_1_dd.selected_option == 'kilometres':
			curr_opt_1 = 'km'
		elif opt_1_dd.selected_option == 'inches':
			curr_opt_1 = 'inch'
		elif opt_1_dd.selected_option == 'yards':
			curr_opt_1 = 'yd'
		elif opt_1_dd.selected_option == 'miles':
			curr_opt_1 = 'mile'
		else:
			pass

		# get curr_opt_2 in abbreviated for to use for conversion
		if opt_2_dd.selected_option == 'centimetres':
			curr_opt_2 = 'cm'
		elif opt_2_dd.selected_option == 'metres':
			curr_opt_2 = 'm'
		elif opt_2_dd.selected_option == 'kilometres':
			curr_opt_2 = 'km'
		elif opt_2_dd.selected_option == 'inches':
			curr_opt_2 = 'inch'
		elif opt_2_dd.selected_option == 'yards':
			curr_opt_2 = 'yd'
		elif opt_2_dd.selected_option == 'miles':
			curr_opt_2 = 'mile'
		else:
			pass

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					# convert and display
					if event.ui_element == convert_btn:

						out_box.set_text('')
						user_text = inp_box.get_text()

						try:
							converter = length(float(user_text), curr_opt_1, curr_opt_2)
						except ValueError:
							user_text = '0'
							converter = length(float(user_text), curr_opt_1, curr_opt_2)

						comp_text = str(round(converter.convert(), 5))
						out_box.set_allowed_characters(
						['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
						out_box.set_text(comp_text)
						out_box.set_allowed_characters([])

					if event.ui_element == inp_box:
						user_text = inp_box.get_text()

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
			manager_dd.process_events(event)
		manager.update(time_delta)
		manager_dd.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		manager.draw_ui(display)
		manager_dd.draw_ui(display)
		pygame.display.flip()

# speed conversion window / screen
def speed_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'speed'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Speed')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
	manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
	display.fill(dark_orange)

	user_text = ''
	# input space for user to enter numbers to be converted
	inp_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((50, 250), (250, 50)),
	manager = manager, object_id = '#input_boxes')

	comp_text = ''
	# output space where converted number is shown
	out_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((480, 250), (250, 50)),
	manager = manager, object_id = '#output_boxes')

	# conversion from
	curr_opt_1 = 'kmph'
	opt_1_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['kms/hour', 'miles/hour', 'knots'], starting_option = \
	'kms/hour', relative_rect = pygame.Rect((50, 325), (270, 75)),
	manager = manager_dd)

	# conversion to
	curr_opt_2 = 'mph'
	opt_2_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['kms/hour', 'miles/hour', 'knots'], starting_option = \
	'miles/hour', relative_rect = pygame.Rect((480, 325), (270, 75)),
	manager = manager_dd)

	# convert button clicked in order to conver
	convert_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((325, 150), (130, 60)),
	text = 'Convert', manager = manager, object_id = '#convert')

	inp_box.set_allowed_characters(
	['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
	out_box.set_allowed_characters([])

	while True:

		# get curr_opt_1 in abbreviated for to use for conversion
		if opt_1_dd.selected_option == 'kms/hour':
			curr_opt_1 = 'kmph'
		elif opt_1_dd.selected_option == 'miles/hour':
			curr_opt_1 = 'mph'
		elif opt_1_dd.selected_option == 'knots':
			curr_opt_1 = 'kts'
		else:
			pass

		# get curr_opt_2 in abbreviated for to use for conversion
		if opt_2_dd.selected_option == 'kms/hour':
			curr_opt_2 = 'kmph'
		elif opt_2_dd.selected_option == 'miles/hour':
			curr_opt_2 = 'mph'
		elif opt_2_dd.selected_option == 'knots':
			curr_opt_2 = 'kts'
		else:
			pass

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					# convert and display
					if event.ui_element == convert_btn:

						out_box.set_text('')
						user_text = inp_box.get_text()

						try:
							converter = speed(float(user_text), curr_opt_1, curr_opt_2)
						except ValueError:
							user_text = '0'
							converter = speed(float(user_text), curr_opt_1, curr_opt_2)

						comp_text = str(round(converter.convert(), 5))
						out_box.set_allowed_characters(
						['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
						out_box.set_text(comp_text)
						out_box.set_allowed_characters([])

					if event.ui_element == inp_box:
						user_text = inp_box.get_text()

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
			manager_dd.process_events(event)
		manager.update(time_delta)
		manager_dd.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		manager.draw_ui(display)
		manager_dd.draw_ui(display)
		pygame.display.flip()

# temperature conversion window / screen
def temp_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'temp'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Temperature')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
	manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
	display.fill(dark_orange)

	user_text = ''
	# input space for user to enter numbers to be converted
	inp_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((50, 250), (250, 50)),
	manager = manager, object_id = '#input_boxes')

	comp_text = ''
	# output space where converted number is shown
	out_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((480, 250), (250, 50)),
	manager = manager, object_id = '#output_boxes')

	# conversion from
	curr_opt_1 = 'c'
	opt_1_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['celsius', 'fahrenheit', 'kelvin'], starting_option = \
	'celsius', relative_rect = pygame.Rect((50, 325), (270, 75)),
	manager = manager_dd)

	# conversion to
	curr_opt_2 = 'f'
	opt_2_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['celsius', 'fahrenheit', 'kelvin'], starting_option = \
	'fahrenheit', relative_rect = pygame.Rect((480, 325), (270, 75)),
	manager = manager_dd)

	# convert button clicked in order to conver
	convert_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((325, 150), (130, 60)),
	text = 'Convert', manager = manager, object_id = '#convert')

	inp_box.set_allowed_characters(
	['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
	out_box.set_allowed_characters([])

	while True:

		# get curr_opt_1 in abbreviated for to use for conversion
		if opt_1_dd.selected_option == 'celsius':
			curr_opt_1 = 'c'
		elif opt_1_dd.selected_option == 'fahrenheit':
			curr_opt_1 = 'f'
		elif opt_1_dd.selected_option == 'kelvin':
			curr_opt_1 = 'k'
		else:
			pass

		# get curr_opt_2 in abbreviated for to use for conversion
		if opt_2_dd.selected_option == 'celsius':
			curr_opt_2 = 'c'
		elif opt_2_dd.selected_option == 'fahrenheit':
			curr_opt_2 = 'f'
		elif opt_2_dd.selected_option == 'kelvin':
			curr_opt_2 = 'k'
		else:
			pass

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					# convert and display
					if event.ui_element == convert_btn:

						out_box.set_text('')
						user_text = inp_box.get_text()

						try:
							converter = temperature(float(user_text), curr_opt_1, curr_opt_2)
						except ValueError:
							user_text = '0'
							converter = temperature(float(user_text), curr_opt_1, curr_opt_2)

						comp_text = str(round(converter.convert(), 5))
						out_box.set_allowed_characters(
						['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
						out_box.set_text(comp_text)
						out_box.set_allowed_characters([])

					if event.ui_element == inp_box:
						user_text = inp_box.get_text()

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
			manager_dd.process_events(event)
		manager.update(time_delta)
		manager_dd.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		manager.draw_ui(display)
		manager_dd.draw_ui(display)
		pygame.display.flip()

# currency conversion window / screen
def currency_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'currency'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Currency')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
	manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
	display.fill(dark_orange)

	user_text = ''
	# input space for user to enter numbers to be converted
	inp_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((50, 250), (250, 50)),
	manager = manager, object_id = '#input_boxes')

	comp_text = ''
	# output space where converted number is shown
	out_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((480, 250), (250, 50)),
	manager = manager, object_id = '#output_boxes')

	# conversion from
	curr_opt_1 = 'aed'
	opt_1_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['AED', 'USD', 'GBP'], starting_option = \
	'AED', relative_rect = pygame.Rect((50, 325), (270, 75)),
	manager = manager_dd)

	# conversion to
	curr_opt_2 = 'usd'
	opt_2_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['AED', 'USD', 'GBP'], starting_option = \
	'USD', relative_rect = pygame.Rect((480, 325), (270, 75)),
	manager = manager_dd)

	# convert button clicked in order to conver
	convert_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((325, 150), (130, 60)),
	text = 'Convert', manager = manager, object_id = '#convert')

	inp_box.set_allowed_characters(
	['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
	out_box.set_allowed_characters([])

	while True:

		# get curr_opt_1 in abbreviated for to use for conversion
		curr_opt_1 = opt_1_dd.selected_option.lower()

		# get curr_opt_2 in abbreviated for to use for conversion
		curr_opt_2 = opt_2_dd.selected_option.lower()

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					# convert and display
					if event.ui_element == convert_btn:

						out_box.set_text('')
						user_text = inp_box.get_text()

						url = str.__add__('http://data.fixer.io/api/latest?access_key=', APIs.fixer_API)

						try:
							converter = currency(url)
						except ValueError:
							user_text = '0'
							converter = currency(url)

						comp_text = str(converter.convert(float(user_text), curr_opt_1, curr_opt_2))
						out_box.set_allowed_characters(
						['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-'])
						out_box.set_text(comp_text)
						out_box.set_allowed_characters([])

					if event.ui_element == inp_box:
						user_text = inp_box.get_text()

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
			manager_dd.process_events(event)
		manager.update(time_delta)
		manager_dd.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		manager.draw_ui(display)
		manager_dd.draw_ui(display)
		pygame.display.flip()

# calendar conversion window / screen
def cal_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'cal'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	display.blit(background, (0, 0))
	pygame.display.set_caption('Calendar')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
	manager_dd = pygame_gui.UIManager(display_size, 'themes/dropdown_menu_themes.json')
	display.fill(dark_orange)

	# conversion from
	curr_opt_1 = 'gregorian'
	opt_1_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['gregorian', 'julian'], starting_option = \
	'gregorian', relative_rect = pygame.Rect((18, 10), (270, 75)),
	manager = manager_dd)

	# Day number (1 - 31)
	title_text_font = pygame.font.Font('fonts/Montserrat-Bold.ttf', 30)
	text_surf_day, text_rect_day = text_objects('Day No. (1 - 31)', title_text_font, black)
	text_rect_day.center = (130, 145)
	# Day input
	day_number_text = ''
	day_number_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((17, 180), (220, 50)),
	manager = manager, object_id = '#input_boxes')

	# Month
	text_surf_month, text_rect_month = text_objects('Month (1 - 12)', title_text_font, black)
	text_rect_month.center = (390, 145)
	# Month input
	month_text = 'Jan'
	month_number_text = ''
	month_number_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((282, 180), (220, 50)),
	manager = manager, object_id = '#input_boxes')

	# Year
	text_surf_year, text_rect_year = text_objects('Year', title_text_font, black)
	text_rect_year.center = (655, 145)
	# Year input
	year_text = ''
	year_box = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((550, 180), (220, 50)),
	manager = manager, object_id = '#input_boxes')

	# conversion to
	curr_opt_2 = 'julian'
	opt_2_dd = pygame_gui.elements.UIDropDownMenu(
	options_list = ['gregorian', 'julian'], starting_option = \
	'julian', relative_rect = pygame.Rect((18, 385), (270, 75)),
	manager = manager_dd)

	# Day number (1 - 31) 2
	text_surf_day_2, text_rect_day_2 = text_objects('Day No. (1 - 31)', title_text_font, black)
	text_rect_day_2.center = (130, 520)
	# Day input 2
	day_number_text_2 = ''
	day_number_box_2 = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((17, 555), (220, 50)),
	manager = manager, object_id = '#input_boxes')

	# Month number (1 - 12) 2
	text_surf_month_2, text_rect_month_2 = text_objects('Month (1 - 12)', title_text_font, black)
	text_rect_month_2.center = (390, 520)
	# Month input 2
	month_text_2 = 'Jan'
	month_number_text_2 = ''
	month_number_box_2 = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((282, 555), (220, 50)),
	manager = manager, object_id = '#input_boxes')

	# Year 2
	text_surf_year_2, text_rect_year_2 = text_objects('Year', title_text_font, black)
	text_rect_year_2.center = (655, 520)
	# Year input 2
	year_text_2 = ''
	year_box_2 = pygame_gui.elements.UITextEntryLine(
	relative_rect = pygame.Rect((550, 555), (220, 50)),
	manager = manager, object_id = '#input_boxes')

	# convert button clicked in order to conver
	convert_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((18, 280), (130, 60)),
	text = 'Convert', manager = manager, object_id = '#convert')

	numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

	# only allowed to enter numbers - dates
	day_number_box.set_allowed_characters(numbers_list)
	month_number_box.set_allowed_characters(numbers_list)
	year_box.set_allowed_characters(numbers_list)

	day_number_box_2.set_allowed_characters([])
	month_number_box_2.set_allowed_characters([])
	year_box_2.set_allowed_characters([])

	# can't enter more than 2 ints
	day_number_box.set_text_length_limit(2)
	month_number_box.set_text_length_limit(2)

	day_number_box_2.set_text_length_limit(2)
	month_number_box_2.set_text_length_limit(2)

	while True:

		# get curr_opt_1 for to use for conversion
		if opt_1_dd.selected_option == 'julian':
			curr_opt_1 = 'julian'
		elif opt_1_dd.selected_option == 'gregorian':
			curr_opt_1 = 'gregorian'
		else:
			pass

		# get curr_opt_2 to use for conversion
		if opt_2_dd.selected_option == 'julian':
			curr_opt_2 = 'julian'
		elif opt_2_dd.selected_option == 'gregorian':
			curr_opt_2 = 'gregorian'
		else:
			pass

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# month has to be between 1 and 12
		try:
			if int(month_number_box.get_text()) > 12 or int(month_number_box.get_text()) < 1:
				month_number_box.set_text('')
		except ValueError:
			pass

		# can't have more days than is actually in the month
		try:
			if int(month_number_box.get_text()) in [1, 3, 5, 7, 8, 10, 12]:
				if int(day_number_box.get_text()) > 31 or int(day_number_box.get_text()) < 1:
					day_number_box.set_text('')
			elif int(month_number_box.get_text()) in [4, 6, 9, 11]:
				if int(day_number_box.get_text()) > 30 or int(day_number_box.get_text()) < 1:
					day_number_box.set_text('')
			elif int(month_number_box.get_text()) == 2:
				if int(day_number_box.get_text()) > 29 or int(day_number_box.get_text()) < 1:
					day_number_box.set_text('')
			else:
				pass
		except ValueError:
			pass

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					# convert and display
					if event.ui_element == convert_btn:

						# clear output
						day_number_box_2.set_text('')
						month_number_box_2.set_text('')
						year_box_2.set_text('')

						dates_list = [day_number_box.get_text(), \
						month_number_box.get_text(), year_box.get_text()]

						# initialize
						converter = calendar(curr_opt_1, curr_opt_2, dates_list)

						dates_list_2 = converter.convert()

						# allow to show text
						day_number_box_2.set_allowed_characters(numbers_list)
						month_number_box_2.set_allowed_characters(numbers_list)
						year_box_2.set_allowed_characters(numbers_list)

						# put final conversion in output
						day_number_box_2.set_text(str(dates_list_2[0]))
						month_number_box_2.set_text(str(dates_list_2[1]))
						year_box_2.set_text(str(dates_list_2[2]))

						# make output uneditable
						day_number_box_2.set_allowed_characters([])
						month_number_box_2.set_allowed_characters([])
						year_box_2.set_allowed_characters([])

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
			manager_dd.process_events(event)
		manager.update(time_delta)
		manager_dd.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		display.blit(text_surf_day, text_rect_day)
		display.blit(text_surf_month, text_rect_month)
		display.blit(text_surf_year, text_rect_year)
		display.blit(text_surf_day_2, text_rect_day_2)
		display.blit(text_surf_month_2, text_rect_month_2)
		display.blit(text_surf_year_2, text_rect_year_2)

		manager.draw_ui(display)
		manager_dd.draw_ui(display)
		pygame.display.flip()


# used to choose which screen to run
user_wdw, user_prev, user_curr = True, prev_screen, curr_screen

# driver code
if __name__ == "__main__":

	# first initialization - start on intro page
	user_wdw, user_prev, user_curr = introduction(user_prev, user_curr)

	# choose which screen to run as long as not quitting
	while user_wdw is not False:
		user_wdw, user_prev, user_curr = screen_to_run(user_wdw, user_prev, user_curr)

# close everything
pygame.quit()
sys.exit()
