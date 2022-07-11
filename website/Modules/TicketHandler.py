#from website.Modules.Google.Google import Google

import datetime
import pytz


class TicketHandler:
	def __init__(self, new_booking):
		self.ticket = self._create_ticket(new_booking)

	def handle_ticket(self):
		
		if self.ticket:
			self._add_ticket_to_system()
			return self.ticket
	
	def _add_ticket_to_system(self):
		# add ticket to google sheets
		#Google().add_booking(self.ticket)
		pass

	def _ticket_is_valid(self, ticket):
		"""set database for all known sellers"""
		# validate seller
		seller_id = ticket['Seller ID']
		"""
		if seller_id not in database:
			return None
		"""
		return True

	def _create_ticket(self, new_booking):
		
		tz = pytz.timezone('Asia/Phnom_Penh')
		id = datetime.datetime.now(tz)
		string = '{}{}{}{}{}'.format(id.month, id.day, id.hour, id.minute, id.second)
		
		ticket = {
			'Booking ID': string, 
			'Seller ID': new_booking['seller_id'],
			
			'Status': 'new booking',

			'Date of Trip': new_booking['date'], 
			'Desired time': new_booking['time'],
			'Departure': new_booking['departure'],
			'Pick up': new_booking['pick_up'],
			'Destination': new_booking['destination'],
			'Drop off': new_booking['drop_off'],
			'Car type': new_booking['car_type'],
			'Seats': new_booking['seats'],
			'Price': '',
			'Payment Status': 'pending',
			
			'customer name': new_booking['customer_name'],
			'Passport No.': new_booking['passport_number'],
			"What's APP": new_booking['whats_app_phone_number'],
			"Telegram": new_booking['telegram_phone_number'],
			"Facebook": new_booking['facebook_name'],
			"Email": new_booking['email'],
			'Luggage': new_booking['luggage'],
			'Payment Option': new_booking['payment_option'],
			
			'Date of Booking': id.strftime("%Y-%m-%d %H:%M"),
			
			
			'Notes': new_booking['notes']
			}

		if self._ticket_is_valid(ticket):
			return ticket
		else:
			return None
		
		
		
		

