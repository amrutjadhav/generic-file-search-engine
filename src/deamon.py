import time
import pdb
import sys
import pyinotify  # import pynotify  

# custom modules import
from databasehandler import DatabaseHandler

class DeepSearchHandler(pyinotify.ProcessEvent):
	""" Deep file search handler to handle the events gengerated by file changes """
	def __init__(self):	
		self.datahandler = DatabaseHandler()
		# self._ignore_directories = False
		# self._ignore_patterns = False
		# self._ignore_patterns = ["*.log","*.logger"]
		# self._case_sensitive = False
		# self._patterns = ["*.rb","*.py","*.java","*.mp4","*.mp3","*.txt"]
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

	def close_db_connection(self):
		""" call close_connection function of datanadler """
		self.datahandler.close_connection()

if __name__=='__main__':
	args = sys.argv[1:]
	directory_path = "/home/atom/Pictures/"
	watch_manager = pyinotify.WatchManager()
	if args:
		directory_path = args[0]
	watch_manager.add_watch(directory_path,pyinotify.ALL_EVENTS,rec=True)
	handler = DeepSearchHandler()
	notifier = pyinotify.Notifier(watch_manager, handler)

	notifier.loop()

	handler.close_db_connection()					#close db connection finally

	print("Deep file search deamon terminated")