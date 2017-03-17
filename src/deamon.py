__author__ = "Amrut Jadhav"
__credits__ = ["Amrut Jadhav"]
__license__ = "MIT"
__maintainer__ = "Amrut Jadhav"
__email__ = "amrutjadhav2294@gmail.com"
__status__ = "Development"


import time
import sys
import pyinotify  # import pynotify  

# custom modules import
from databasehandler import DatabaseHandler

class DeepSearchHandler(pyinotify.ProcessEvent):
	""" Deep file search handler to handle the events gengerated by file changes """
	def __init__(self):	
		self.datahandler = DatabaseHandler()
		print "instance created"


	def process_IN_CREATE(self,event):
		"""Called when a file or directory is created."""
		print "file create event"+str(event)
		self.datahandler.create(event.pathname)		

	def process_IN_MODIFY(self,event):
		""""Called when a file or directory is modified."""
		print "file modify event"+str(event)
		self.datahandler.update(event.pathname)

	def process_IN_DELETE(self,event):
		"""" Called when a file or directory is deleted. """
		print "file delete event"+str(event)
		self.datahandler.delete(event.pathname)

	def process_IN_ACCESS(self,event):
		"""" Called when a file or directory is accessed. """
		print "file access event"+str(event.pathname)
		self.datahandler.access(event.pathname)

	def close_db_connection(self):
		""" call close_connection function of datanadler """
		self.datahandler.close_connection()

if __name__=='__main__':
	args = sys.argv[1:]
	directory_path = "/home/atom/Pictures/"
	if args:
		directory_path = args[0]

	watch_manager = pyinotify.WatchManager()			# Define watch manager
	watch_manager.add_watch(directory_path,pyinotify.ALL_EVENTS,rec=True)	# Add watch to directory
	handler = DeepSearchHandler()						# Create object of handler class	
	notifier = pyinotify.Notifier(watch_manager, handler)  	# Build notifier

	notifier.loop()								# Listen to events recursively 

	handler.close_db_connection()					#close db connection after loop is break

	print("Deep file search deamon terminated")