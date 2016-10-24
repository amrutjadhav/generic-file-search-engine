import sys
import time

from watchdog.observers import Observer                   # import observer 
from watchdog.events import PatternMatchingEventHandler	 

class DeepSearchHadnler(object):
	""" Deep file search handler to handle the events gengerated by file changes """
	def __init__(self):	
		patterns = ["*.rb","*.py","*.java","*.mp4","*.mp3"]
		

if __name__=='__main__':
	directory_path = "/home/atom/workspace/pytom"
	observer = Observer()
	observer.schedule(DeepSearchHadnler(),directory_path)	# Scheduling the handler
	observer.start()
	
	try:
		while True:
			time.sleep(10)
	except KeyboardInterrupt:								# Stop execution if ctrl+'c' hits teminal
		observer.stop()
	finally:
		print("Deep file search deamon terminated")

	observer.join()											#	wait till thread joins