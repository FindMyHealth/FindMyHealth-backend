# imports
from lxml import html
import requests
import mysql.connector
import time

# database credentials
my_host = "localhost"
my_username = "root"
my_password = ""
my_database = "health"

# establish MySQL connection
cnx = mysql.connector.connect(user=my_username, password=my_password,host=my_host,database=my_database)
cursor = cnx.cursor()

# pull all states data
def find_all_states():
	
	# pull first page
	page = requests.get("https://projects.propublica.org/emergency/")
	print page
	tree = html.document_fromstring(page.text)

	all_state_data = []

	for val in tree.xpath("//div[contains(@class, 'state-container element')]"):
		
		ind_state_data = []

		ind_state_data.append(str(val.xpath("div/span/a/text()")[0]))
		ind_state_data.append(str(val.xpath("div/span/a/@href")[0]))

		# adds state name/link to MySQL
		try:
			ind_state_data.append(str(val.xpath("div[@class='state-box state-box-door']/span/text()")[0]))
		except:
			ind_state_data.append("-1")

		try:
			ind_state_data.append(str(val.xpath("div[@class='state-box large state-box-op18 wide']/span/text()")[0]))
		except:
			ind_state_data.append("-1")

		try:
			ind_state_data.append(str(val.xpath("div[@class='state-box state-box-bone']/span/text()")[0]))
		except:
			ind_state_data.append("-1")

		try:
			ind_state_data.append(str(val.xpath("div[@class='state-box state-box-ed2']/span/text()")[0]))
		except:
			ind_state_data.append("-1")
	
		cursor.execute("INSERT INTO states_averages (state_name, state_link, waiting_time, time_until_sent_home, broken_bone, transfer_time) VALUES (%s, %s, %s, %s, %s, %s)",())
			
		all_state_data.append(ind_state_data)

	print all_state_data

		# cursor.execute("INSERT INTO states_averages_basic (state_name, state_link) VALUES (%s, %s)", (str(val.xpath("div[@class = 'state-name state-box state-box-name']/a/text()")[0]), str(val.xpath("div[@class='state-name state-box state-box-name']/a/@href")[0])))
				

find_all_states()
cnx.commit()
