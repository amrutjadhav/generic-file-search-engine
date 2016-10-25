import sys
import time
import os       # file system related functionality
import MongoConnection
import pymongo  # mongodb python driver

from watchdog.observers import Observer                   # import observer 
from watchdog.events import PatternMatchingEventHandler	 

class FileStatHandler:
	""" class to extract and get files attributes """
	def get_inode(self,src_path):
		""" return inode of file """
		return os.stat(src_path).ST_INO

	def get_modified_time(self,src_path):
		""" return modified time of file """
		return os.stat(src_path).ST_MTIME


class DatabaseHandler:
	""" class to make changes in the db according the event"""
	def __init__(self):
		""" Init mongodb connection"""
		connection = MongoConnection()
		db = connection.fileengine
		collection = db.meta
		file_handler = FileStatHandler()

	def file_present?(self,inode):
		""" check if file is present in the database"""
		if collection.find({inode:inode}):
			return True
		else:
			return False

	def update_modified_time(self,src_path):
		""" update only modified time of file """
		inode = file_handler.get_inode(src_path)
		file_modified_time = file_handler.get_modified_time(src_path)
		collection.update_one({inode:inode},$set:{modified_time:file_modified_time})


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