# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:28:19 2022

@author: Harish
"""

#Essential libraries
from selenium import webdriver     #Required to drive chrome automatically
import math as mat          #Needed for few calculations
import time          #Required to produce delay in successive steps


#Download and locate the chromedriver in your PC and paste it's path
location_of_chromedriver_in_your_system="C:/Users/Harish/Downloads/chromedriver.exe"
driver = webdriver.Chrome(location_of_chromedriver_in_your_system)


#Go to WOS, search your requirement and copy the generated query
query_copied_from_WOS='https://www.webofscience.com/wos/woscc/summary/05fbfdd2-80f1-4e67-b698-bd04ed1d40d6-6789c2f5/relevance/1'
driver.get(query_copied_from_WOS)
time.sleep(7)

#To delete the dialogue box just at entrence 
dialogue=driver.find_elements_by_xpath('//*[@id="pendo-close-guide-5600f670"]')[0].click()
time.sleep(6)


#An additional dialogue box deleter just go and copy and Paste Xpath here
#dilog=driver.find_elements_by_xpath('Paste Xpath here')[0].click()
#time.sleep(4)


#To get total number of documents, just to identify total number of loops required
get= driver.find_elements_by_xpath('//*[@id="mat-checkbox-1"]/label/span[2]')[0].text
aa= int(get.translate ({ord(x): "" for x in "!@#$%^&*()[]{};:,./<>?\|`'\"~-=-+"}))
time.sleep(1)
number_of_loops=mat.ceil(aa/500)

a=1      #from in first loop  initially =1
b=500      #To in first loop    initially =500


try:
    for i in range(number_of_loops):
        export= driver.find_elements_by_xpath('//*[@id="snRecListTop"]/app-export-menu/div/button/span[1]')[0].click()
        time.sleep(2)
        
        plain=driver.find_elements_by_xpath('//*[@id="exportToFieldTaggedButton"]')[0].click()
        time.sleep(3)
        
        record= driver.find_elements_by_xpath('//*[@id="radio3"]/label/span[2]')[0].click()
        time.sleep(4)
        
        content=driver.find_elements_by_xpath('/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/div[1]/wos-select/button')[0].click()
        time.sleep(8)
        
        cr=driver.find_elements_by_xpath('//*[@id="global-select"]/div/div[2]/div[4]/span')[0].click()
        time.sleep(5)
    
        
        ii=2*i
        key1='//*[@id="mat-input-'+str (ii)+'"]'
        count1=driver.find_elements_by_xpath(key1)[0].clear()
        #time.sleep(1)
        count1=driver.find_elements_by_xpath(key1)[0].send_keys(a)
        #time.sleep(1)
      
    
        jj=2*i+1
        key2='//*[@id="mat-input-'+str (jj)+'"]'
        count2=driver.find_elements_by_xpath(key2)[0].clear()
        #time.sleep(1)
        count2=driver.find_elements_by_xpath(key2)[0].send_keys(b)
        time.sleep(2)
        
        
        export= driver.find_elements_by_xpath('/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/div[2]/button[1]/span[1]/span')[0].click() 
        time.sleep(10)
        a=a+500
        b=b+500
    print('Downloading Completed')
except:
    print(f'Downloading failed in between! please restart the program with initial value of a as {a} and b as {b}')
