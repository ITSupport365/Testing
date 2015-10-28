modified by jagan !testing!

import urllib2
import re
import pymssql
from re import findall
import operator
import MySQLdb
import datetime
from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from random import randrange
from dateutil.relativedelta import relativedelta

db = MySQLdb.connect(host="202.129.198.139", port=3306, user="root",passwd="365media", db="StorageTrack")
cursor=db.cursor()
print "\nconnected"


dp = pymssql.connect(host=r"54.227.255.185:1436", user='sa', password='data2go', database='maximrms')
connect = dp.cursor()
print "connect"


cursor.execute("Select Proxy from Proxy_List")
resultset = cursor.fetchall()
for i in range(1):
    irand = randrange(0, 10)
    proxy_id = resultset[irand]
    proxy1 = proxy_id[0]
    print proxy1
    
    
myProxy = proxy1   
proxy = Proxy({
'proxyType': ProxyType.MANUAL,
'httpProxy': myProxy,
'ftpProxy': myProxy,
'sslProxy': myProxy,
'noProxy':''})


main_url = ('http://www.hotelsjianguo.com/jianguo_garden_hotel/en-us/')
driver = webdriver.Firefox(proxy=proxy)
driver.get(main_url)
time.sleep(3)

today = datetime.date.today()

one_day = datetime.timedelta(days=1)

HotelCode = "07"
PulledDate = datetime.date.today()
ratetype = ''
RoomType = ''
Channel = 'BTG-JIANGUO Hotels & Resorts'
Length_of_Stay  = '1'
ArrivalDate = ''
Guests = '2'
Status = ''
QuoteRate = ''
CurrencyCode = 'CNY'
Description = ''
LowestRateFlag = ''
Tax = ''
RoomCharges = ''
Fees = ''
HotelBlock = ''
HotelId = ''
HotelVariantid = ''
TotalPrice = ''
URL = ''


for i in range(30):
	RateTyp = ''
	RoomType = ''
	ArrivalDate = ''
	QuoteRate = ''
	Description = ''
	HotelBlock = ''
	TotalPrice = ''
	URL = ''
	print "\nDays:",today
	dt1 = today
	days = today.strftime("%a")
	print days
	if "Wed" in days:
		day = "WED"
	elif "Mon" in days:
		day = "MON"
	elif "Sun" in days:
		day = "SUN"
	elif "Fri" in days:
		day = "FRI"
	elif "Thu" in days:
		day = "THU"
	elif "Sat" in days:
		day = "SAT"
	elif "Tue" in days:
		day = "TUE"
	print day
	adt = str(today)+" "+str(day)
	print adt
	time.sleep(1)
	driver.execute_script('document.getElementById("entrance-check-in").removeAttribute("readonly")')
	driver.find_element_by_xpath('//input[@id="entrance-check-in"]').clear()
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="entrance-check-in"]').send_keys(adt)
	tl = today+ one_day
	today = tl
	days = today.strftime("%a")
	print days
	if "Wed" in days:
		day = "WED"
	elif "Mon" in days:
		day = "MON"
	elif "Sun" in days:
		day = "SUN"
	elif "Fri" in days:
		day = "FRI"
	elif "Thu" in days:
		day = "THU"
	elif "Sat" in days:
		day = "SAT"
	elif "Tue" in days:
		day = "TUE"
	print day
	ddt = str(today)+" "+str(day)
	print ddt
	time.sleep(1)
	driver.execute_script('document.getElementById("entrance-check-out").removeAttribute("readonly")')
	driver.find_element_by_xpath('//input[@id="entrance-check-out"]').clear()
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="entrance-check-out"]').send_keys(ddt)
	
	
	x_path = '//span[@class="ui-btn-text"]' 
	select_click = driver.find_element_by_xpath(x_path)
	select_click.click()
	time.sleep(15)
	
	x_path = '//a[@data-value="All Room Types^Shrink All the Room Types"]' 
	select_click = driver.find_element_by_xpath(x_path)
	if select_click:
		select_click.click()
		time.sleep(15)
		html=driver.page_source
		html = html.encode('ascii','ignore')
		#print html

		reg_block = re.compile(r'<div class="ui-accordion-heading js-room-head">(.*?)</div>\s*</div>\s*</div>\s*</div>',re.DOTALL)
		Reg_bl = re.compile(r'<tr class=".*?-item">\s*<td class="type-caption">(.*?)</a>\s*</td>\s*</tr>',re.DOTALL)
		Roomty = (r'<i class="icon-room-info"></i>(.*?)</span>')
		price = (r'</dfn><span>(.*?)</span>\s*</span>')
		Ratetype = (r'<span class="type-item">(.*?)</span>\s*</td>')
		Zipcode = (r'onclick="recalcula_precios\(this\);" />\s*(F.*?)</div>')
		description = (r'<i class="icon-room-info"></i>\s*(.*?)\s*</span>')
		#Phone_no = (r'"phoneDesc">.*?</span>\s*<span>\s*(.*?)\s*</span> ',re.DOTALL)

		for block in reg_block.findall(html):
			#print block
			blo = re.sub("'","''",block)
			for block1 in Reg_bl.findall(block):
				#print block1		
					
				pri = re.search(Roomty,block)
				if pri:
					p = pri.group(1)
					print "\nRoomType:",p
					
					
						
				spe = re.search(price,block1)
				if spe:
					sp1 = spe.group(1)
					sp = re.sub('&amp;','',sp1)
					print "\nPrice:",sp
					
					
				des = re.search(Ratetype,block1,re.DOTALL)
				if des:
					d = des.group(1)
					ratety1 = re.sub(r'<.*?>|\n|\s*','',d)
					ratety = reduce(operator.add,ratety1)
					print "\nRatetype:",ratety
					
					
				des1 = re.search(Zipcode,block1)
				if des1:
					d1 = des1.group(1)
					print "\nZipCode:",d1
					
				
				des2 = re.search(description,block1)
				if des2:
					d2 = des2.group(1)
					rate = re.sub('<.*?>','',d2)
					print "\nDescription:",rate
				
				pho = re.search('"phoneDesc">.*?</span>\s*<span>\s*(.*?)\s*</span> ',block,re.DOTALL)
				if pho:
					ph = pho.group(1)
					print "\nPhone_No:",ph
				print "\n-------------------------^^^^^^^^^^^^^^^^^^^^^^^^^---------------------------\n"
				print ("INSERT Into maximrms.dbo.Python_HotelRawData(HotelCode,PulledDate,RateType,RoomType,Channel,Length_of_Stay,ArrivalDate,Guests,Status,QuoteRate,CurrencyCode,Description,LowestRateFlag,Tax,RoomCharges,Fees,HotelBlock,HotelVariantid,TotalPrice,URL) values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(HotelCode,PulledDate,ratety,p,Channel,Length_of_Stay,dt1,Guests,Status,sp,CurrencyCode,rate,LowestRateFlag,Tax,RoomCharges,Fees,blo,HotelVariantid,sp,main_url))
				cursor.execute ("INSERT Into maximrms.dbo.Python_HotelRawData(HotelCode,PulledDate,RateType,RoomType,Channel,Length_of_Stay,ArrivalDate,Guests,Status,QuoteRate,CurrencyCode,Description,LowestRateFlag,Tax,RoomCharges,Fees,HotelBlock,HotelVariantid,TotalPrice,URL) values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(HotelCode,PulledDate,ratety,p,Channel,Length_of_Stay,dt1,Guests,Status,sp,CurrencyCode,rate,LowestRateFlag,Tax,RoomCharges,Fees,blo,HotelVariantid,sp,main_url))
				dp.commit()
			print "\n---------------------%%%%%%%%$$$$$$$$%%%%%%%%%-------------------------\n"
	else:
	    print "There is no data"
	driver.back()
	time.sleep(5)


for i in range(9):
	RateTyp = ''
	RoomType = ''
	ArrivalDate = ''
	QuoteRate = ''
	Description = ''
	HotelBlock = ''
	TotalPrice = ''
	URL = ''
	print "\nWeeks:",today
	dt1 = today
	days = today.strftime("%a")
	print days
	if "Wed" in days:
		day = "WED"
	elif "Mon" in days:
		day = "MON"
	elif "Sun" in days:
		day = "SUN"
	elif "Fri" in days:
		day = "FRI"
	elif "Thu" in days:
		day = "THU"
	elif "Sat" in days:
		day = "SAT"
	elif "Tue" in days:
		day = "TUE"
	print day
	adt = str(today)+" "+str(day)
	print adt
	time.sleep(1)
	driver.execute_script('document.getElementById("entrance-check-in").removeAttribute("readonly")')
	driver.find_element_by_xpath('//input[@id="entrance-check-in"]').clear()
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="entrance-check-in"]').send_keys(adt)
	tr = today+ one_day
	days = tr.strftime("%a")
	print days
	if "Wed" in days:
		day = "WED"
	elif "Mon" in days:
		day = "MON"
	elif "Sun" in days:
		day = "SUN"
	elif "Fri" in days:
		day = "FRI"
	elif "Thu" in days:
		day = "THU"
	elif "Sat" in days:
		day = "SAT"
	elif "Tue" in days:
		day = "TUE"
	print day
	ddt = str(tr)+" "+str(day)
	print ddt
	time.sleep(1)
	driver.execute_script('document.getElementById("entrance-check-out").removeAttribute("readonly")')
	driver.find_element_by_xpath('//input[@id="entrance-check-out"]').clear()
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="entrance-check-out"]').send_keys(ddt)
	tl = today+ datetime.timedelta(weeks=1)
	today = tl
	
	x_path = '//span[@class="ui-btn-text"]' 
	select_click = driver.find_element_by_xpath(x_path)
	select_click.click()
	time.sleep(15)
	
	x_path = '//a[@data-value="All Room Types^Shrink All the Room Types"]' 
	select_click = driver.find_element_by_xpath(x_path)
	if select_click:
		select_click.click()
		time.sleep(15)
		html=driver.page_source
		html = html.encode('ascii','ignore')
		#print html

		reg_block = re.compile(r'<div class="ui-accordion-heading js-room-head">(.*?)</div>\s*</div>\s*</div>\s*</div>',re.DOTALL)
		Reg_bl = re.compile(r'<tr class=".*?-item">\s*<td class="type-caption">(.*?)</a>\s*</td>\s*</tr>',re.DOTALL)
		Roomty = (r'<i class="icon-room-info"></i>(.*?)</span>')
		price = (r'</dfn><span>(.*?)</span>\s*</span>')
		Ratetype = (r'<span class="type-item">(.*?)</span>\s*</td>')
		Zipcode = (r'onclick="recalcula_precios\(this\);" />\s*(F.*?)</div>')
		description = (r'<i class="icon-room-info"></i>\s*(.*?)\s*</span>')
		#Phone_no = (r'"phoneDesc">.*?</span>\s*<span>\s*(.*?)\s*</span> ',re.DOTALL)

		for block in reg_block.findall(html):
			#print block
			blo = re.sub(r"'","''",block)
			for block1 in Reg_bl.findall(block):
				#print block1		
					
				pri = re.search(Roomty,block)
				if pri:
					p = pri.group(1)
					print "\nRoomType:",p
					
					
						
				spe = re.search(price,block1)
				if spe:
					sp1 = spe.group(1)
					sp = re.sub('&amp;','',sp1)
					print "\nPrice:",sp
					
					
				des = re.search(Ratetype,block1,re.DOTALL)
				if des:
					d = des.group(1)
					ratety1 = re.sub(r'<.*?>|\n|\s*','',d)
					ratety = reduce(operator.add,ratety1)
					print "\nRatetype:",ratety
					
					
				des1 = re.search(Zipcode,block1)
				if des1:
					d1 = des1.group(1)
					print "\nZipCode:",d1
					
				
				des2 = re.search(description,block1)
				if des2:
					d2 = des2.group(1)
					rate = re.sub('<.*?>','',d2)
					print "\nDescription:",rate
				
				pho = re.search('"phoneDesc">.*?</span>\s*<span>\s*(.*?)\s*</span> ',block,re.DOTALL)
				if pho:
					ph = pho.group(1)
					print "\nPhone_No:",ph
				print "\n-------------------------^^^^^^^^^^^^^^^^^^^^^^^^^---------------------------\n"
				print ("INSERT Into maximrms.dbo.Python_HotelRawData(HotelCode,PulledDate,RateType,RoomType,Channel,Length_of_Stay,ArrivalDate,Guests,Status,QuoteRate,CurrencyCode,Description,LowestRateFlag,Tax,RoomCharges,Fees,HotelBlock,HotelVariantid,TotalPrice,URL) values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(HotelCode,PulledDate,ratety,p,Channel,Length_of_Stay,dt1,Guests,Status,sp,CurrencyCode,rate,LowestRateFlag,Tax,RoomCharges,Fees,blo,HotelVariantid,sp,main_url))
				cursor.execute ("INSERT Into maximrms.dbo.Python_HotelRawData(HotelCode,PulledDate,RateType,RoomType,Channel,Length_of_Stay,ArrivalDate,Guests,Status,QuoteRate,CurrencyCode,Description,LowestRateFlag,Tax,RoomCharges,Fees,HotelBlock,HotelVariantid,TotalPrice,URL) values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(HotelCode,PulledDate,ratety,p,Channel,Length_of_Stay,dt1,Guests,Status,sp,CurrencyCode,rate,LowestRateFlag,Tax,RoomCharges,Fees,blo,HotelVariantid,sp,main_url))
				dp.commit()
			print "\n---------------------%%%%%%%%$$$$$$$$%%%%%%%%%-------------------------\n"
	else:
		print "There is no data"
	driver.back()
	time.sleep(5)

for i in range(9):
	RateTyp = ''
	RoomType = ''
	ArrivalDate = ''
	QuoteRate = ''
	Description = ''
	HotelBlock = ''
	TotalPrice = ''
	URL = ''
	print "\nMonths:",today
	dt1 = today
	days = today.strftime("%a")
	print days
	if "Wed" in days:
		day = "WED"
	elif "Mon" in days:
		day = "MON"
	elif "Sun" in days:
		day = "SUN"
	elif "Fri" in days:
		day = "FRI"
	elif "Thu" in days:
		day = "THU"
	elif "Sat" in days:
		day = "SAT"
	elif "Tue" in days:
		day = "TUE"
	print day
	adt = str(today)+" "+str(day)
	print adt
	time.sleep(1)
	driver.execute_script('document.getElementById("entrance-check-in").removeAttribute("readonly")')
	driver.find_element_by_xpath('//input[@id="entrance-check-in"]').clear()
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="entrance-check-in"]').send_keys(adt)
	tr = today+ one_day
	days = tr.strftime("%a")
	print days
	if "Wed" in days:
		day = "WED"
	elif "Mon" in days:
		day = "MON"
	elif "Sun" in days:
		day = "SUN"
	elif "Fri" in days:
		day = "FRI"
	elif "Thu" in days:
		day = "THU"
	elif "Sat" in days:
		day = "SAT"
	elif "Tue" in days:
		day = "TUE"
	print day
	ddt = str(tr)+" "+str(day)
	print ddt
	time.sleep(1)
	driver.execute_script('document.getElementById("entrance-check-out").removeAttribute("readonly")')
	driver.find_element_by_xpath('//input[@id="entrance-check-out"]').clear()
	time.sleep(2)
	driver.find_element_by_xpath('//input[@id="entrance-check-out"]').send_keys(ddt)
	tl = today + relativedelta(months=1)
	today = tl
	x_path = '//span[@class="ui-btn-text"]' 
	select_click = driver.find_element_by_xpath(x_path)
	select_click.click()
	time.sleep(50)
	x_path = '//a[@data-value="All Room Types^Shrink All the Room Types"]' 
	select_click = driver.find_element_by_xpath(x_path)
	if select_click:
		select_click.click()
		time.sleep(15)
		html=driver.page_source
		html = html.encode('ascii','ignore')
		reg_block = re.compile(r'<div class="ui-accordion-heading js-room-head">(.*?)</div>\s*</div>\s*</div>\s*</div>',re.DOTALL)
		Reg_bl = re.compile(r'<tr class=".*?-item">\s*<td class="type-caption">(.*?)</a>\s*</td>\s*</tr>',re.DOTALL)
		Roomty = (r'<i class="icon-room-info"></i>(.*?)</span>')
		price = (r'</dfn><span>(.*?)</span>\s*</span>')
		Ratetype = (r'<span class="type-item">(.*?)</span>\s*</td>')
		Zipcode = (r'onclick="recalcula_precios\(this\);" />\s*(F.*?)</div>')
		description = (r'<i class="icon-room-info"></i>\s*(.*?)\s*</span>')
		#Phone_no = (r'"phoneDesc">.*?</span>\s*<span>\s*(.*?)\s*</span> ',re.DOTALL)
		for block in reg_block.findall(html):
			#print block
			blo = re.sub(r"'","''",block)
			for block1 in Reg_bl.findall(block):
				#print block1		
				pri = re.search(Roomty,block)
				if pri:
					p = pri.group(1)
					print "\nRoomType:",p		
				spe = re.search(price,block1)
				if spe:
					sp1 = spe.group(1)
					sp = re.sub('&amp;','',sp1)
					print "\nPrice:",sp	
				des = re.search(Ratetype,block1,re.DOTALL)
				if des:
					d = des.group(1)
					ratety1 = re.sub(r'<.*?>|\n|\s*','',d)
					ratety = reduce(operator.add,ratety1)
					print "\nRatetype:",ratety
				des1 = re.search(Zipcode,block1)
				if des1:
					d1 = des1.group(1)
					print "\nZipCode:",d1
				des2 = re.search(description,block1)
				if des2:
					d2 = des2.group(1)
					rate = re.sub('<.*?>','',d2)
					print "\nDescription:",rate
				pho = re.search('"phoneDesc">.*?</span>\s*<span>\s*(.*?)\s*</span> ',block,re.DOTALL)
				if pho:
					ph = pho.group(1)
					print "\nPhone_No:",ph
				print "\n-------------------------^^^^^^^^^^^^^^^^^^^^^^^^^---------------------------\n"
				print ("INSERT Into maximrms.dbo.Python_HotelRawData(HotelCode,PulledDate,RateType,RoomType,Channel,Length_of_Stay,ArrivalDate,Guests,Status,QuoteRate,CurrencyCode,Description,LowestRateFlag,Tax,RoomCharges,Fees,HotelBlock,HotelVariantid,TotalPrice,URL) values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(HotelCode,PulledDate,ratety,p,Channel,Length_of_Stay,dt1,Guests,Status,sp,CurrencyCode,rate,LowestRateFlag,Tax,RoomCharges,Fees,blo,HotelVariantid,sp,main_url))
				cursor.execute ("INSERT Into maximrms.dbo.Python_HotelRawData(HotelCode,PulledDate,RateType,RoomType,Channel,Length_of_Stay,ArrivalDate,Guests,Status,QuoteRate,CurrencyCode,Description,LowestRateFlag,Tax,RoomCharges,Fees,HotelBlock,HotelVariantid,TotalPrice,URL) values( '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(HotelCode,PulledDate,ratety,p,Channel,Length_of_Stay,dt1,Guests,Status,sp,CurrencyCode,rate,LowestRateFlag,Tax,RoomCharges,Fees,blo,HotelVariantid,sp,main_url))
				dp.commit()
			print "\n---------------------%%%%%%%%$$$$$$$$%%%%%%%%%-------------------------\n"
	else:
		print "There is no data"
	driver.back()
	time.sleep(5)
