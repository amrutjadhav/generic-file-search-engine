import sys
import pymongo  # mongodb python driver

class MongoConnection(object):
	"""docstring for MongoConnection"""
	def __init__(self):
		client = MongoClient()
		db = client.fileengine

if __name__=='__main__':
	connection = MongoConnection()
		
