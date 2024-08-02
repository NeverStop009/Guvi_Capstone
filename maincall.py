from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep


service = Service(executable_path='./driver/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.redbus.in")

sleep(10)
print("----------------------------------------------------------------------------------------------------------------------------------------------")


ids = driver.find_elements("class name",'rtcBack')
coun = 0;
for ii in ids:
    coun = coun + 1
    print("--")    
    idsa = ii.find_elements("tag name", 'li')
    print(str(coun),".",ii.find_element("class name",'rtcName').text)
    
    

state_No = input("Please enter an integer: ")


elem = driver.find_element("xpath",'//*[@id="Carousel"]/div['+state_No+']')
action = ActionChains(driver)   
action.move_to_element(elem).click().perform() 
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
       
sleep(10)
driver2 = webdriver.Chrome(service=service, options=options)
driver2.get(pglink)
sleep(10)
