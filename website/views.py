from flask import Blueprint, render_template, request, flash
from website.Modules.TicketHandler import TicketHandler


views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		ticket = TicketHandler(request.form).handle_ticket()
		if ticket:
			flash("success", category='success')
			return render_template("home.html",data=ticket)
		else:
			flash("invalid Seller ID", category='error')
			return render_template("home.html")

	if request.method == 'GET':
		return render_template("home.html")
	
