import logging
import tailer
import time

class LogReader():

	def readLog():
		
		#take file and read the last line
		file = tailer.tail(open('myLogFile.txt', 'w') ,1)
		#follow the file as it grows
		for line in tailer.follow(open('myLogFil.txt')):
			print(line)







