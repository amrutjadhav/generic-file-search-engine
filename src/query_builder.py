import re 

# Import custom helpers
from query_helper import Helper
from databasehandler import DatabaseHandler

class QueryBuilder(Exception):
	
	def __init__(self):
		""" Initialize """
		self.databasehandler = DatabaseHandler()
		self.helper = Helper()
		print("Hello there..! Query about your system files..")

	def builder(self,user_query):
		""" Build db query parsing user's query """ 
		file_tense = self.find_tense(user_query)			# Return +1/-1 
		timestamp,timestamp_query = self.find_time_query(user_query)  # Return date & [day/month/year]
		file_mode = self.find_file_mode(user_query)		# Return [create/modify/delete]=[0,4,9]
		result = self.build_query(file_tense,timestamp,timestamp_query,file_mode)
		if result:
			for doc in result:
				print(doc["name"])
		else:
			print("Sorry, I don't found any related files")

	def build_query(self,file_tense,timestamp,timestamp_query,file_mode):
		""" Build mongodb query """
		if file_tense < 0:
			timestamp-=1

		if file_mode == 0:
			# db.meta.aggregate({$project:{name:1,month:{$month:'$create'}}},{$match:{month:11}})
			return self.databasehandler.execute_query(timestamp_query,"$"+timestamp_query,"$create",timestamp)
		elif file_mode == 4:
			return  self.databasehandler.execute_query(timestamp_query,"$"+timestamp_query,"$modify",timestamp)
		elif file_mode == 9:
			return  self.databasehandler.execute_query(timestamp_query,"$"+timestamp_query,"$delete",timestamp)


	def find_time_query(self,user_query):
		""" Return time"""
		if "day" in user_query:
			 return self.helper.get_present_day(),"dayOfMonth"
		elif "month" in user_query:
			return self.helper.get_present_month(),"month"
		elif "year" in user_query:
			return  self.helper.get_present_year(),"year"
		else:
			raise Exception("Specify search date operator i.e day,month,year")

	def find_tense(self,user_query):
		""" Find the tense of user query """
		past_tense_literals = ["last","previous","ago"]
		present_tense_literals = ["this","present","today"]
		if any(literal in user_query for literal in past_tense_literals):
			return -1
		elif any(literal in user_query for literal in present_tense_literals):
			return  1
		else:
			raise Exception("Specify tense i.e previous,today etc.")

	def find_file_mode(self,user_query):
		""" Return file search mode """
		if "create" in user_query:
			return 0
		elif "modif" in user_query:
			return 4
		elif "delete" in user_query:
			return 9
		else:
			raise Exception("Specify file mode i.e create,modify,delete")

	# def find_days(self,user_query):
	# 	""" Find the days of user query """ 
	# 	if re.search('\d',user_query):
	# 		return re.search('\d',user_query).group()
	# 	elif:
	# 		retur None

if __name__=='__main__':
	query_builder = QueryBuilder()
	while True:
		try:
			query = raw_input("Enter your query = ")
			query_builder.builder(query)
		except Exception as e:								
			print("[Error]=>"+str(e))
		except KeyboardInterrupt:								# Stop execution if ctrl+'c' hits teminal
			query_builder.databasehandler.close_connection()
			print("Deep file search engine terminated")
			break
