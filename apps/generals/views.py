"""Generals views"""

# Django
from django.shortcuts import render, redirect

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


def index(request):
	ctx = {
	}
	return render(request, 'index.html', ctx)