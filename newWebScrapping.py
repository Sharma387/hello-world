import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from lxml import html
import requests

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

print DRIVER_BIN

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

#Load the main page.
#driver.get('http://s15.a2zinc.net/clients/MJBiz/Fall17MJBizCon/Public/Exhibitors.aspx?ID=261&sortMenu=104001')

#Loop the entire page to get the details printed for all the rows

for i in range(1,99,1):
    # Load the main page.
    driver.get('http://s15.a2zinc.net/clients/MJBiz/Fall17MJBizCon/Public/Exhibitors.aspx?ID=261&sortMenu=104001')

    #select the second row from the table
    xPathLink = '//*[@id="ctl00_dvContent"]/div[11]/div[1]/div/div/div[3]/div/table/tbody/tr[' + str(i) +']/td[2]/a'
    print xPathLink
    driver.find_element_by_xpath(xPathLink).click()

    #driver.get('http://s15.a2zinc.net/clients/MJBiz/Fall17MJBizCon/Public/eBooth.aspx?IndexInList=1&FromPage=Exhibitors.aspx&ParentBoothID=&ListByBooth=true&BoothID=105225')
    #page = requests.get('http://s15.a2zinc.net/clients/MJBiz/Fall17MJBizCon/Public/eBooth.aspx?IndexInList=1&FromPage=Exhibitors.aspx&ParentBoothID=&ListByBooth=true&BoothID=105225')

    page = requests.get(driver.current_url)
    #//*[@id="ctl00_dvContent"]/div[11]/div[1]/div/div/div[3]/div/table/tbody/tr[2]/td[2]/a


    #driver.get('http://s15.a2zinc.net/clients/MJBiz/Fall17MJBizCon/Public/eBooth.aspx?Task=&IndexInList=3&FromPage=Exhibitors.aspx&BoothID=104735&Upgraded=&SortMenu=')
    #page = requests.get('http://s15.a2zinc.net/clients/MJBiz/Fall17MJBizCon/Public/eBooth.aspx?Task=&IndexInList=3&FromPage=Exhibitors.aspx&BoothID=104735&Upgraded=&SortMenu=')
    #tree = html.fromstring(page.content)
    tree = html.fromstring(page.content)
    #tree = html.fromstring(page.text)
    #print tree1

    #This will create a list of buyers:
    #buyers = tree.xpath('//div[@title=""]/text()')
    exhibitor_name = tree.xpath('//*[@id="eboothContainer"]/div[2]/div/h1/text()')

    #Address
    # City
    exhibitor_city = tree.xpath('//*[@id="eboothContainer"]/div[2]/div/div[1]/span[1]/text()')

    # State
    exhibitor_state = tree.xpath('//*[@id="eboothContainer"]/div[2]/div/div[1]/span[2]/text()')
    # Country
    exhibitor_country = tree.xpath('//*[@id="eboothContainer"]/div[2]/div/div[1]/span[3]/text()')

    #Company URL
    exhibitor_url = tree.xpath('//*[@id="BoothContactUrl"]/text()')



    exhibitor_facebook = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_dlCustomFieldList_ctl00_lnkCustomField"]/@href')

    exhibitor_tweeter = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_dlCustomFieldList_ctl01_lnkCustomField"]/@href')
    exhibitor_linkedin = tree.xpath('//*[@id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_dlCustomFieldList_ctl02_lnkCustomField"]/@href')

    print exhibitor_name
    print exhibitor_city
    print exhibitor_state
    print exhibitor_country
    print exhibitor_facebook
    print exhibitor_linkedin
    print exhibitor_tweeter
    print exhibitor_url



#CLick on the back button or reload the page
 #   driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lnkBackToSearch"]').click()


    #driver.find_element_by_class_name()

    #increment i by 1 for next element

#time.wait(4)
#driver.close()


#//*[@id="ctl00_dvContent"]/div[11]/div[1]/div/div/div[3]/div/table/tbody/tr[2]/td[2]/a"
#//*[@id="ctl00_dvContent"]/div[10]/div[1]/div/div/div[3]/div/table/tbody/tr[2]/td[2]/a