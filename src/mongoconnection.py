import sys
import pymongo  # mongodb python driver

class MongoConnection(object):
	"""docstring for MongoConnection"""
	def __init__(self):
		__client = MongoClient()

if __name__=='__main__':
	connection = MongoConnection()
		
