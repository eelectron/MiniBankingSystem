from django.urls import path, include
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("login/", views.login, name="login"),
	path("logout/", views.logout, name="logout"),
	path("register/", views.register, name="register"),
	path("addAddress/", views.addAddress, name="address"),
	path("createAccount/", views.createAccount, name="account"),
	path("transfer/", views.transfer, name="transfer"),
	path("mainPage/", views.mainPage, name="mainPage"),
]