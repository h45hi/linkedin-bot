from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
		
	def search_for(self,position):
		position.strip(' ')
		bot = self.bot
		search_url = bot.get(URL+'search/results/people/?keywords='+position+'&origin=SWITCH_SEARCH_VERTICAL')

	def download_resume(self):
		bot = self.bot
		# bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		profiles = bot.find_elements_by_class_name("search-result__result-link")
		unique_links = []

		for person in profiles:
			link = person.get_attribute('href')
			if link not in unique_links:
					unique_links.append(link)

		for link in unique_links:
			bot.get(link)
			time.sleep(5)
			more = bot.find_element_by_class_name("pv-s-profile-actions__overflow-toggle.artdeco-button").click()
			time.sleep(2)
			save_pdf = bot.find_element_by_class_name("pv-s-profile-actions--save-to-pdf").click()
			time.sleep(5)
				

t = LinkedinBot('kumarnisit@gmail.com', 'HPiZ_CuwsD5$dqT')
t.login()
time.sleep(5)
t.search_for('Deepak')
time.sleep(5)
t.download_resume()