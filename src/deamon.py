import sys
import time
import os       # file system related functionality

# custom modules import
from databasehandler import DatabaseHandler

from watchdog.observers import Observer                   # import observer 
from watchdog.events import PatternMatchingEventHandler	 

class DeepSearchHandler(PatternMatchingEventHandler):
	""" Deep file search handler to handle the events gengerated by file changes """
	def __init__(self):	
		patterns = ["*.rb","*.py","*.java","*.mp4","*.mp3","*.txt","*","*.c","*.cpp"]
		datahandler = DatabaseHandler()

	def on_created(self,event):
		"""Called when a file or directory is created."""
		datahandler.create(event.src_path)		

	def on_modified(self,event):
		""""Called when a file or directory is modified."""
		datahandler.update(event.src_path)

	def on_deleted(self,event):
		"""" Called when a file or directory is deleted. """
		datahandler.delete(event.src_path)

	def on_moved(self,event):
		""""Called when a file or a directory is moved or renamed."""
		datahandler.moved(event.src_path)

if __name__=='__main__':
	directory_path = "/home/atom/workspace/pytom"
	observer = Observer()
	observer.schedule(DeepSearchHandler(),directory_path)	# Scheduling the handler
	observer.start()
	
	try:
		while True:
			time.sleep(10)
	except KeyboardInterrupt:								# Stop execution if ctrl+'c' hits teminal
		observer.stop()
	finally:
		print("Deep file search deamon terminated")

	observer.join()											#	wait till thread joins