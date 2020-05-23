from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def users_list(request):
	users_list = User.objects.values('id', 'username', 'first_name', 
		'last_name', 'email', 'is_active').all()
	ctx = {
		'users_list':users_list,
	}
	return render(request, 'users_list.html', ctx )