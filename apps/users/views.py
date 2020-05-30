"""Users views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Local imports



def users_list(request):
	users_list = User.objects.values('id', 'username', 'first_name', 
		'last_name', 'email', 'is_active').all()
	ctx = {
		'users_list':users_list,
	}
	return render(request, 'users_list.html', ctx )



@login_required()
@transaction.atomic
def create_user(request):
	if request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			try:
				user = form.save()
				user.refresh_from_db()  # load the profile instance created by the signal
				user.is_active = True
				#user.email = user.username
				#user.profile.auth_phone = request.POST['auth_phone']
				#user.profile.auth_email_confirmed = True
				#user.profile.auth_revise_sol_ventas = request.POST['auth_revise_sol_ventas']
				user.save()
				for x in request.POST.getlist('grupos'):
					g = Group.objects.get(id=x)
					g.user_set.add(user)
				messages.success(request, 'Usuario creado con éxito')
			except expression as identifier:
				messages.error(
					request, 'Ocurrió un problema al crear usuario, por favor revise los datos ingresados.')
				grupos = Group.objects.all()
				ctx = {
					'grupos': grupos,
					'form': form
				}
				return render(request, 'usuarios_crear.html', ctx)
		else:
			messages.error(
				request, 'Ocurrió un problema al crear usuario, por favor revise los datos ingresados')
			grupos = Group.objects.all()
			ctx = {
				'form': form,
				'grupos': grupos
			}
			return render(request, 'usuarios_crear.html', ctx)
		return redirect('usuarios_listado')
	form = SignUpForm()
	grupos = Group.objects.all()
	ctx = {
		'grupos': grupos,
		'form': form
	}
	return render(request, 'crear_usuario.html', ctx)