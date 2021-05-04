from django.db import models

# Create your models here.

'''
	This stores all customers of this bank .
'''
class Customer(models.Model):
	userName = models.CharField(max_length=128, unique=True)
	firstName = models.CharField(max_length=128)
	lastName =  models.CharField(max_length=128)
	email = 	models.CharField(max_length=128)
	phone = 	models.CharField(max_length=128)
	password =  models.CharField(max_length=128)

	# completed, pending, blocked, error
	verificationStatus = models.CharField(max_length=128)

	def __str__(self):
		return f"{self.userName}, {self.firstName}, {self.lastName}, {self.email}"

'''
	Every address maps to an existing customer .
'''
class Address(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
	line1 = models.CharField(max_length=256)
	line2 = models.CharField(max_length=256)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=128)
	pincode = models.IntegerField()

'''
	Every account maps to a existing customer .
	Accounts can of different type for ex. Saving, Current, Fixed etc
'''
class Account(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
	typeOfAccount = models.CharField(max_length=128)
	balance = models.DecimalField(max_digits=256, decimal_places=4)
	interest = models.DecimalField(max_digits=8, decimal_places=4)

'''
	Transactions of accounts are saved in this table
'''
class Transaction(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
	creationDate = models.DateTimeField()
	typeOfTransaction = models.CharField(max_length=64)
	balance = models.DecimalField(max_digits=256, decimal_places=4)

