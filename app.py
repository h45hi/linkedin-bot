from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.facebook.com'
class FacebookBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get(URL)
		time.sleep(5)
		email = bot.find_element_by_name('email')
		password = bot.find_element_by_name('pass')
		email.send_keys(self.username)
		password.send_keys(self.password)
		sign_in = bot.find_element_by_id('loginbutton')
		sign_in.send_keys(Keys.RETURN)
		time.sleep(5) # _3_16 _6a-y _3l2t  _18vj

	def like(self,search_text):
		bot = self.bot
		bot.get(URL+'/search/posts/?q='+search_text+'&epa=SERP_TAB')


t = FacebookBot('rajivg774@gmail.com', 'rajiv9871')
t.login()
t.like('naruto uzumaki')