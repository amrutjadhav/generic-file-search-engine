import sys
import time
import MongoConnection
import pymongo  # mongodb python driver

from watchdog.observers import Observer                   # import observer 
from watchdog.events import PatternMatchingEventHandler	 

class DatabaseHandler:
	""" class to make changes in the db according the event"""
	def __init__(self):
		""" Init mongodb connection"""
		connection = MongoConnection()
		db = connection.fileengine

	def file_present?(self,inode):
		""" check if file is present in the database"""
		if db.meta.find({inode:inode}):
			return True
		else:
			return False
			

class DeepSearchHandler(object):
	""" Deep file search handler to handle the events gengerated by file changes """
	def __init__(self):	
		patterns = ["*.rb","*.py","*.java","*.mp4","*.mp3"]

	def on_created:
		"""Called when a file or directory is created."""

	def on_modified:
		""""Called when a file or directory is modified."""

	def on_deleted:
		"""" Called when a file or directory is deleted. """


	def on_moved:
		""""Called when a file or a directory is moved or renamed."""


		

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