import os
import sys
import time

class FileStatHandler:
	""" class to extract and get files attributes """
	def get_name(self,src_path):
		""" return name of file/directory """
		head,tail = os.path.split(src_path)
		return tail
	
	def get_directory(self,src_path):
		""" return directory of file """
		return os.path.dirname(src_path)

	def is_directory(self,src_path):
		""" return true is path is directory else false """
		return os.path.isdir(src_path)

	def get_inode(self,src_path):
		""" return inode of file """
		return os.stat(src_path).st_ino

	def get_extension(self,src_path):
		""" return file extension """
		if not self.is_directory(src_path):
			file_name , file_extension = os.path.splitext(src_path)
			return file_extension

	def get_path(self,src_path):
		""" return path of file """
		return src_path

	def get_size(self,src_path):
		""" return file size in bytes """
		return os.path.getsize(src_path)

	def get_modified_time(self,src_path):
		""" return modified time of file """
		return date_time_conversion(os.path.getmtime(src_path))

	def get_accessed_time(self,src_path):
		""" return last accessed time of file """
		return date_time_conversion(os.path.getatime(src_path))
	
	def get_creation_time(self,src_path):
		""" return file creation time """
		return date_time_conversion(os.path.getctime(src_path))

	def date_time_conversion(self,epoch_seconds):
		""" return the datetime value of milliseconds"""
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_seconds))