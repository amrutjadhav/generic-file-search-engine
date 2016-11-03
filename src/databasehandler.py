from mongoconnection import MongoConnection
import pymongo  # mongodb python driver

class DatabaseHandler:
	""" class to make changes in the db according the event"""
	def __init__(self):
		""" Init mongodb connection"""
		connection = MongoConnection()
		collection = connection.db.meta
		file_handler = FileStatHandler()

	def create(self,src_path):
		""" add new file entry into db """

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
