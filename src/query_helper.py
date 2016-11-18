__author__ = "Amrut Jadhav"
__credits__ = ["Amrut Jadhav"]
__license__ = "MIT"
__maintainer__ = "Amrut Jadhav"
__email__ = "amrutjadhav2294@gmail.com"
__status__ = "Development"


""" This helper provide time conversions facilities """
import time
import datetime

class Helper:
	def __init__(self):
		""" Initialize now to present """
		self.now = datetime.datetime.now() 
	
	def get_present_day(self):
		""" Return present date """
		return self.now.day

	def get_present_month(self):
		""" Return present date """
		return self.now.month

	def get_present_year(self):
		""" Return present year """
		return self.now.year


	