import os
import sys

class FileStatHandler:
	""" class to extract and get files attributes """
	def get_inode(self,src_path):
		""" return inode of file """
		return os.stat(src_path).ST_INO

	def get_modified_time(self,src_path):
		""" return modified time of file """
		return os.stat(src_path).ST_MTIME
	