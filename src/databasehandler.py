__author__ = "Amrut Jadhav"
__credits__ = ["Amrut Jadhav"]
__license__ = "MIT"
__maintainer__ = "Amrut Jadhav"
__email__ = "amrutjadhav2294@gmail.com"
__status__ = "Development"

import pdb #python debugger
from pymongo import MongoClient # mongodb python driver

# import custom module 
from filestatHandler import FileStatHandler

class DatabaseHandler:
	""" class to make changes in the db according the event"""
	def __init__(self):
		""" Init mongodb connection"""
		self.client = MongoClient()
		self.db = self.client.fileengine
		self.collection = self.db.meta
		self.file_handler = FileStatHandler()

	def create(self,src_path):
		""" add new file entry into db """
		self.collection.insert_one({"name":self.file_handler.get_name(src_path), "inode":self.file_handler.get_inode(src_path),
				"extension":self.file_handler.get_extension(src_path), "path":self.file_handler.get_path(src_path),
				"parent":self.file_handler.get_directory(src_path), "directory":self.file_handler.is_directory(src_path),
				"create":self.file_handler.get_creation_time(src_path), "access":self.file_handler.get_accessed_time(src_path),
				"modify":self.file_handler.get_modified_time(src_path), "size": self.file_handler.get_size(src_path),
				"access_count":1,"status":"create"})

	def is_file_present(self,src_path):
		""" check if file is present in the database"""
		if self.collection.find({"path":src_path,"status":{"$ne": "delete"}}):
			return True
		else:
			return False

	def update(self,src_path):
		""" update only modified time of file """
		if not self.is_file_present(src_path):
			create(src_path)
		# inode = self.file_handler.get_inode(src_path)
		file_modified_time = self.file_handler.get_modified_time(src_path)
		updated_size = self.file_handler.get_size(src_path) 
		self.collection.update_one({"path":src_path,"status":{"$ne": "delete"}},
									{"$set":{"modify":file_modified_time,"status":"modify","size":updated_size}})

	def delete(self,src_path):
		""" update the status of file which is deleted """
		if self.is_file_present(src_path):
			self.collection.update_one({"path":src_path,"status":{"$ne": "delete"}},{"$set":{"status": "delete"}})

	def access(self,src_path):
		""" increaments accessed count of file """
		if not self.is_file_present:
			create(src_path)
		self.collection.update_one({"path":src_path},{"$inc":{"access_count":1}})

	def close_connection(self):
		""" close database connection """
		self.client.close()

	def execute_query(self,timestamp_query,date_operator,date_object,timestamp):
		""" Execute the file find query on db """
		file_result = self.collection.aggregate([{"$project":{"name":1,timestamp_query:{date_operator:date_object}}},{"$match":{timestamp_query:timestamp}}])
		return file_result