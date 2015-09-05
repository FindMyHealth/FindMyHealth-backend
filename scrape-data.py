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

base_url = "https://projects.propublica.org" 

# pull all states data
def find_hospital_data(state, url):
	
	# pull first page
	page = requests.get(base_url + url)
	tree = html.document_fromstring(page.text)

	for val in tree.xpath("//div[contains(@class, 'state-container element')]"):
		
		ind_state_data = []

		ind_state_data.append(state)
		ind_state_data.append(str(val.xpath("div/a/text()")[0]))
		ind_state_data.append(str(val.xpath("div/a/@href")[0]))

		# adds state name/link to MySQL
		try:
			ind_state_data.append(str(val.xpath("div[@class='state-box state-box-door']/span/text()")[0]))
		except:
			ind_state_data.append("-1")

		try:
			ind_state_data.append(str(val.xpath("div[contains(@class,'state-box large state-box-op18 wide')]/span/text()")[0]))
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

		try:	
			individual_hospital = requests.get(base_url + ind_state_data[2])
			individual_tree = html.document_fromstring(individual_hospital.text)
	
			for node in individual_tree.xpath("//div[@class='vitals']"):
				ind_state_data.append(str(node.xpath("div[@class='hosp-phone']/p/text()")[0]))
				ind_state_data.append(" ".join(node.xpath("div[@class='address']/p/text()")))
	
			cursor.execute("INSERT INTO states_averages (state_name, hospital_name, hospital_link, waiting_time, time_until_sent_home, broken_bone, transfer_time, phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(ind_state_data[0], ind_state_data[1], ind_state_data[2], ind_state_data[3], ind_state_data[4], ind_state_data[5], ind_state_data[6], ind_state_data[7], ind_state_data[8]))			
			print ind_state_data
		except:
			print "Skipped!"	


data = []
cursor.execute("SELECT * FROM states_averages_basic")
data = cursor.fetchall()

for point in data:
	find_hospital_data(point[1], point[2])

cnx.commit()

