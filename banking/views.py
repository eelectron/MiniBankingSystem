from django.shortcuts import render

from django.contrib.auth.hashers import make_password

from . models import Customer


# Create your views here.

'''
Show the main page
'''
def index(request):
	return render(request, "banking/index.html")


'''
	Autheticate the user .
	Logs a user inside website .  
'''
def login(request):
	if request.method == "POST":
		print("login")
	else:
		return render(request, "banking/login.html")

'''
	Logs a user out of website
'''
def logout(request):
	print("logout")
	return render(request, "banking/login.html")

'''
	Registers a user
'''
def register(request):
	if request.method == "POST":
		
		# get the information from form
		userName = request.POST["userName"]
		firstName = request.POST["firstName"]
		lastName = request.POST["lastName"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		password = make_password(request.POST["password"])

		# insert it in DB
		customer = Customer(userName=userName, firstName=firstName, lastName=lastName, email=email, phone=phone, password=password, verificationStatus="verified")
		customer.save()

		return render(request, "banking/login.html")
	else:
		return render(request, "banking/register.html")

'''
	Add address of customer
'''
def addAddress(request):
	print("address")

'''
	Create a account for customer .
	For ex: Savig, Current, Fixed
'''
def createAccount(request):
	print("account")

'''
	Transfer amount from one account to 
	other 
'''
def transfer(request):
	print("transfer")