from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import mysql.connector
from time import sleep

import time


service = Service(executable_path='./driver/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.redbus.in/bus-tickets/vijayawada-to-hyderabad?fromCityId=134&toCityId=124&fromCityName=Vijayawada&toCityName=Hyderabad&busType=Any&onward=01-Aug-2024&srcCountry=null&destCountry=null")
sleep(10)

mydb = mysql.connector.connect(
                  host=" 127.0.0.1",
                  user="root",
                  password="",
                  database="redbus"
        )
mycursor = mydb.cursor()


last = driver.find_element("xpath", '//*[@id="result-section"]/div[2]/div/div[2]/div/div[4]/div[2]')
last.click()


last_height = driver.execute_script("return document.body.scrollHeight")

scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
 
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
  
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
   
    if (screen_height) * i > scroll_height:
        break
 

sleep(5)
def getdata(dataid):
    #div_element = driver.find_element("id",'26762666')
    
   # row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[1]/div[1]')
   
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[1]/div[1]')
    bus_name = row_data.text
    print("BUsname: ", bus_name)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[2]/div[1]')
    bus_type = row_data.text
    print("Bus Type: ", bus_type)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[3]/div')
    starting_time = row_data.text
    print("Starting Time: ", starting_time)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[4]/div[1]')
    duration = row_data.text
    print("Duration: ", duration)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[6]/div/div')
    reaching_time = row_data.text
    print("Reaching Time: ", reaching_time)

    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[6]/div/div/span') 
    #row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[7]/div[1]/span')
    price = row_data.text
    print("Price: ", price)

    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[7]/div[1]')  #//*[@id="26704174"]/div/div[1]/div[1]/div[7]/div[1]
    #row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[6]/div/div/span') 
    seats_available = row_data.text
    print("Seats Available: ", seats_available)



    sql = "INSERT INTO bus_routes (busname, bustype, departing_time, duration, reaching_time, price, seats_available)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (bus_name, bus_type,starting_time,duration,reaching_time,price,seats_available)
    print(sql)
    print (val)
    mycursor.execute(sql, val)
    mydb.commit()
    mylast_id = mycursor.lastrowid
    



    

ul = driver.find_element("class name",'bus-items')
ul = ul.find_elements("tag name",'li')
coun = 0;

for ii in ul:
    if(str(ii.get_attribute('id'))):
        dataid = str(ii.get_attribute('id'))
        getdata(dataid)




