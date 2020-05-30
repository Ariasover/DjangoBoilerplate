"""Generals views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login 
from django.contrib.auth.decorators import login_required


# Local imports


def login(request):
	ctx = {}
	if request.user.is_authenticated:
		print('verificar user',request.user)
		return redirect('generals:index')
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return redirect('generals:index')
		ctx = {
			'error': True,
			'username': username,
		}
	return render(request, 'login.html', ctx)

@login_required()
def index(request):
	ctx = {
	}
	return render(request, 'index.html', ctx)

def logout_user(request):
	logout(request)
	return redirect('generals:login')
