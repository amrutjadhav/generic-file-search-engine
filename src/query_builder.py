import re 

# Import custom helpers
from query_helper import Helper
from databasehandler import DatabaseHandler

class QueryBuilder:
	
	def __init__(self):
		""" Initialize """
		self.databasehandler = DatabaseHandler()
		self.helper = Helper()
		print("query builder class is initialized.")

	def builder(self,user_query):
		""" Build db query parsing user's query """ 
		file_tense = self.find_tense(user_query)			# Return +1/-1 
		timestamp,timestamp_query = self.find_time_query(user_query)  # Return date & [day/month/year]
		file_mode = self.find_file_mode(user_query)		# Return [create/modify/delete]=[0,4,9]
		print(file_tense,timestamp,timestamp_query,file_mode)
		self.build_query(file_tense,timestamp,timestamp_query,file_mode)

	def build_query(self,file_tense,timestamp,timestamp_query,file_mode):
		""" Build mongodb query """
		if file_tense < 0:
			timestamp-=1

		if file_mode == 0:
			# db.meta.aggregate({$project:{name:1,month:{$month:'$create'}}},{$match:{month:11}})
			self.databasehandler.execute_query(timestamp_query,"$"+timestamp_query,"$create",timestamp)
		elif file_mode == 4:
			self.databasehandler.execute_query(timestamp_query,"$"+timestamp_query,"$modify",timestamp)
		elif file_mode == 9:
			self.databasehandler.execute_query(timestamp_query,"$"+timestamp_query,"$delete",timestamp)


	def find_time_query(self,user_query):
		""" Return time"""
		print( user_query)
		if "day" in user_query:
			 return self.helper.get_present_day(),"dayOfMonth"
		elif "month" in user_query:
			return self.helper.get_present_month(),"month"
		elif "year" in user_query:
			return  self.helper.get_present_year(),"year"
		else:
			print("wrong query")

	def find_tense(self,user_query):
		""" Find the tense of user query """
		past_tense_literals = ["last","previous","ago"]
		present_tense_literals = ["this","present","today"]
		if any(literal in user_query for literal in past_tense_literals):
			return -1
		elif any(literal in user_query for literal in present_tense_literals):
			return  1

	def find_file_mode(self,user_query):
		""" Return file search mode """
		if "create" in user_query:
			return 0
		elif "modif" in user_query:
			return 4
		elif "delete" in user_query:
			return 9

	# def find_days(self,user_query):
	# 	""" Find the days of user query """ 
	# 	if re.search('\d',user_query):
	# 		return re.search('\d',user_query).group()
	# 	elif:
	# 		retur None

if __name__=='__main__':
	query_builder = QueryBuilder()
	try:
		while True:
			query = raw_input("Enter your query = ")
			query_builder.builder(query)
	except KeyboardInterrupt:								# Stop execution if ctrl+'c' hits teminal
		query.databasehandler.close_db_connection()
	finally:
		print("Deep file search engine terminated")
