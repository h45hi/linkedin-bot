from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import import ipdb
URL = 'https://www.linkedin.com/'
class LinkedinBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get(URL)
		time.sleep(2)
		sign_in = bot.find_element_by_class_name("nav__button-secondary").click()
		time.sleep(2)
		email = bot.find_element_by_id("username")
		email.send_keys(self.username)
		time.sleep(2)
		password = bot.find_element_by_id("password")
		password.send_keys(self.password)
		time.sleep(2)
		sign_in = bot.find_element_by_class_name("btn__primary--large.from__button--floating").click()
		
	def for_position(self,position):
		ipdb.set_trace()
		position.strip(' ')
		bot = self.bot
		bot.get(URL+'search/results/people/?keywords='+position+'&origin=SWITCH_SEARCH_VERTICAL')


t = LinkedinBot('kumarnisit@gmail.com', 'HPiZ_CuwsD5$dqT')
t.login()
time.sleep(5)
t.for_position('Python Developer')