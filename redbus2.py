from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector
import requests
from time import sleep

import time


service = Service(executable_path='./driver/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
#driver.get("https://www.redbus.in/bus-tickets/vijayawada-to-hyderabad?fromCityId=134&toCityId=124&fromCityName=Vijayawada&toCityName=Hyderabad&busType=Any&onward=30-Jul-2024&srcCountry=null&destCountry=null")
driver.get("https://www.redbus.in")
sleep(10)

divid = driver.find_elements("class name",'rtcBack')
coun = 0;
for ii in divid:
    coun = coun + 1
    print("--")    
    idsa = ii.find_elements("tag name", 'li')
    print(str(coun),".",ii.find_element("class name",'rtcName').text)
    

state_Number = input("Please enter an integer: ")


elementid = driver.find_element("xpath",'//*[@id="Carousel"]/div['+state_Number+']')
action = ActionChains(driver)   
action.move_to_element(elementid).click().perform() 
sleep(5)

print("----------------------lit of pages")

ids = driver.find_element("class name",'DC_117_paginationTable')
ids = ids.find_elements("tag name",'div')
coun = 0;
for ii in ids:    
    print(ii.text)   #//*[@id="root"]/div/div[4]/div[12]/div[2]
    coun = coun + 1    
    action = ActionChains(driver)   
    # perform the operation 
    action.move_to_element(ii).click().perform() 
    sleep(5)
    print("----------------------lit of routes")
    ids = driver.find_elements("class name",'route_link')
    coun = 0;
    for ii in ids:          
        linktext = ''+ ii.find_element("tag name",'a').text
        print(ii.find_element("tag name",'a').get_attribute('href')," : ",linktext)
        pglink = ii.find_element("tag name",'a').get_attribute('href')

        route_link = []
        route_link.append(pglink)
        print("LISTLINK", route_link)

        count = 0
        pagecount = count + 1
       # idpg = ii.find.elements(""
        
page_count_enter = input("Please enter an page: ")

elementid = driver.find_element("xpath",'//*[@id="root"]/div/div[4]/div[12]['+page_count_enter+']')
            
sleep(10)
driver2 = webdriver.Chrome(service=service, options=options)
driver2.get(route_link[page_count_enter])
sleep(10)

route_name = input("Please Enter the from and to Route")

mydb = mysql.connector.connect(
                  host=" 127.0.0.1",
                  user="root",
                  password="",
                  database="redbus"
        )
mycursor = mydb.cursor()


last_height = driver.execute_script("return document.body.scrollHeight")

scroll_pause_time = 1 
screen_height = driver.execute_script("return window.screen.height;")  
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


    #row_data = driver.find_element(BY.XPATH,'//*[@id="'+dataid+'"]/section/div[2]/h1')

    #route_name = row_data.text
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[1]/div[1]')
   
    bus_name = row_data.text
    print("BUsname: ", bus_name)
     
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[1]/div[2]')
    
    bus_type = row_data.text
    print("Bus Type: ", bus_type)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[2]/div[1]')
    
    starting_time = row_data.text
    print("Starting Time: ", starting_time)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[3]/div')
    
    duration = row_data.text
    print("Duration: ", duration)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[4]/div[1]')
    
    reaching_time = row_data.text
    print("Reaching Time: ", reaching_time)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[6]/div')    #//*[@id="24696607"]/div/div[1]/div[1]/div[6]/div
    
    price = row_data.text
    print("Price: ", price)
    
    row_data = driver.find_element(By.XPATH,'//*[@id="'+dataid+'"]/div/div[1]/div[1]/div[7]/div[1]')
    
    seats_available = row_data.text
    print("Seats Available: ", seats_available)

    sql = "INSERT INTO bus_routes (busname, bustype, departing_time, duration, reaching_time, price, seats_available)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (bus_name, bus_type,starting_time,duration,reaching_time,price,seats_available)
    print(sql)
    print (val)
    mycursor.execute(sql, val)
    mydb.commit()
    mylast_id = mycursor.lastrowid

    
    print("____________________________----------",str(mylast_id))

ul = driver.find_element("class name",'bus-items')
ul = ul.find_elements("tag name",'li')
coun = 0;

for ii in ul:
    if(str(ii.get_attribute('id'))):
        dataid = str(ii.get_attribute('id'))
        getdata(dataid)

#INSERT INTO bus_route ( route_name, route_link, busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available)



                
