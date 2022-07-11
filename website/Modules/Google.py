from oauth2client.service_account import ServiceAccountCredentials
from website.Modules.helper import *
import gspread
import os


class Google:
	def __init__(self):
		self.spreadsheet_name = ''  # add your spreadsheet name here
		self.sheet = None

		scope = ["https://spreadsheets.google.com/feeds",
				 'https://www.googleapis.com/auth/spreadsheets',
				 'https://www.googleapis.com/auth/drive.file',
				 "https://www.googleapis.com/auth/drive"]

		#create json file
		create_credentials_file()
		creds = ServiceAccountCredentials.from_json_keyfile_name('./website/Modules/Google/credentials.json', scope)
			
		self.client = gspread.authorize(creds)
		os.remove('./website/Modules/Google/credentials.json') 

	def get_sheet(self):
		sheet_name = "Bookings"  # <--- please set the sheet name here.
		spreadsheet = self.client.open(self.spreadsheet_name)
		self.sheet = spreadsheet.worksheet(sheet_name)
		data = self.sheet.get_all_records()
		return data

	def add_booking(self, new_booking):
		self.get_sheet()
		li = []
		for i in new_booking.keys():
			li.append(new_booking[i])

		self.sheet.insert_row(li, 2)
		