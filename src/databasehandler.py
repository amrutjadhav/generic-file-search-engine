import pdb #python debugger
from pymongo import MongoClient # mongodb python driver

# import custom module 
from filestatHandler import FileStatHandler

class DatabaseHandler:
	""" class to make changes in the db according the event"""
	def __init__(self):
		""" Init mongodb connection"""
		client = MongoClient()
		db = client.fileengine
		collection = db.meta
		file_handler = FileStatHandler()

	def create(self,src_path):
		""" add new file entry into db """
		collection.insert_one({"name":file_handler.get_name(src_path), "inode":file_handler.get_inode(src_path),
				"extension":file_handler.get_extension(src_path), "path":file_handler.get_path(src_path),
				"parent":file_handler.get_directory(src_path), "directory":file_handler.is_directory,
				"create":file_handler.get_creation_time(src_path), "access":file_handler.get_accessed_time(src_path),
				"modify":file_handler.get_modified_time(src_path), "size": file_handler.get_size(src_path),
				"access_count":1})

	def is_file_present(self,inode):
		""" check if file is present in the database"""
		if collection.find({inode:inode}):
			return True
		else:
			return False

	def update(self,src_path):
		""" update only modified time of file """
		inode = file_handler.get_inode(src_path)
		file_modified_time = file_handler.get_modified_time(src_path)
		collection.update({"inode":inode},{"$set":{"modified_time":file_modified_time}})

	def delete(self,src_path):
		""" update the status of file which is deleted """
		if not is_file_present:
			create(src_path)
		inode = file_handler.get_inode(src_path)
		file_modified_time = file_handler.get_modified_time(src_path)
		collection.update_one({"inode":inode},{"$set":{"modified_time":file_modified_time, "status": "delete"}})

	def access(self,src_path):
		""" increaments accessed count of file """
		inode = file_handler.get_inode(src_path)
		access_count = (collection.findOne({"inode":inode},{"_id":0,"access_count":1})) + 1  # fetch and increase access_count
		collection.update_one({"inode":inode},{"$set":{"access_count":access_count}})    # save to database


