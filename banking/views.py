from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

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
		# get info from login form
		userName = request.POST["userName"]
		password = request.POST["password"]

		# check if user is valid
		customer = None
		try:
			# check if userName exist in DB
			customer = Customer.objects.get(userName=userName)

			# check if user have entered correct password
			if check_password(password, customer.password) == False:
				customer = None
		except:
			customer = None
		
		# save customer in session
		if customer is not None:
			print(request)
			return HttpResponseRedirect(reverse('mainPage'))
		else:
			# return to login page with error message
			context = {"message": "Invalid credentials"}
			return render(request, "banking/login.html", context) 
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
		print(request.POST)
		userName = request.POST["userName"]
		firstName = request.POST["firstName"]
		lastName = request.POST["lastName"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		password = make_password(request.POST["password"])

		# insert it in DB
		customer = Customer(userName=userName, firstName=firstName, lastName=lastName, email=email, phone=phone, password=password, verificationStatus="verified")
		customer.save()
		print(customer)
		return HttpResponseRedirect(reverse('login'))
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

'''
Show main page
'''
def mainPage(request):
	context = {"customer": ":)"}
	return render(request, "banking/banking.html", context)