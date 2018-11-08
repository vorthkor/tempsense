import sys
import time
import os
import Adafruit_DHT
import matplotlib.pyplot as plt
import csv
import telepot
from telepot.loop import MessageLoop

address_string = insert

#BOT CONFIG
bot = telepot.Bot("bot id")
bot.sendMessage(address_string, 'running...')

###########

a = 0		#auxiliar variable

#INITIAL MESSAGE
os.system('clear')
os.system('echo hi, interaction {}'.format(a))
plt.ion() 	#interactive mode on
#######

#SENSOR LISTS
#humidity1lis,temperature1lis = [],[]		#zeros subtituted by [] lists
hum1lis = []
tem1lis = []
x = []
hum2lis,tem2lis = [],[]
#########

#CSV FILES
myFile1=open('example1.csv','w')
myFile2 = open('example2.csv','w')
##########

#MAIN LOOP
while True:
	
	bot.sendMessage(address_string, 'interação %a' %a)
	#to terminal plot
	hum1, tem1 = Adafruit_DHT.read_retry(11, 27)
	hum1lis.append(hum1)
	tem1lis.append(tem1)
	print ("S1: Humidity = {} %; Temperature = {} C".format(hum1,tem1))
	bot.sendMessage(address_string, 'temperatura 1: %tem1' %tem1)
	hum2, tem2 = Adafruit_DHT.read_retry(11, 22)
	hum2lis.append(hum2)
	tem2lis.append(tem2)
	print ("S2: Humidity = {} %; Temperature = {} C".format(hum2,tem2))
	bot.sendMessage(address_string, 'temperatura 2: %tem2' %tem2)
	print("\n")
	###################
	
	"""
	DANGER
	"""
	
	if tem1 or tem2 >= 23:
		
    
    #to record in csv file
	with open('example1.csv', 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([hum1, tem1])
	with open('example2.csv', 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([hum2,tem2])
	######################
	
	#Graph plot
	x.append(a)
	a = a + 1
	time.sleep(1)	
	if (a/5) == int(a/5):		#plots after 5 interactions
		os.system('clear')
		os.system('echo hi, interaction {}'.format(a))		#python vars on shell
		'''print(hum1lis,tem1lis)
		print(hum2lis,tem2lis)	'''	#prints the lists values		
		plt.clf() #clears and still paints figures		
		plt.plot(x,hum1lis,'c',linewidth=3,label='Humidity1')
		plt.plot(x,tem1lis,linewidth=5,label='Temperature1')
		plt.plot(x,hum2lis,linewidth=3,label='Humidity2')
		plt.plot(x,tem2lis,'r',linewidth=5,label='Temperature2')
		plt.legend()
		plt.pause(0.05)
		plt.draw()
	plt.show()
	#################
	
	


