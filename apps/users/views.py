"""Users/groups/passwords views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction




# Local imports
from apps.users.forms import SignUpForm




# Users
@login_required()
@transaction.atomic
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
				user.is_active = True
				user.email = user.username
				#user.profile.auth_phone = request.POST['auth_phone']
				#user.profile.auth_email_confirmed = True
				#user.profile.auth_revise_sol_ventas = request.POST['auth_revise_sol_ventas']
				user.save()
				for x in request.POST.getlist('grupos'):
					g = Group.objects.get(id=x)
					g.user_set.add(user)
				messages.success(request, 'Usuario creado con éxito')
			except Exception as e:
				messages.error(
					request, 'Ocurrió un problema al crear usuario, por favor revise los datos ingresados.')
				grupos = Group.objects.all()
				ctx = {
					'grupos': grupos,
					'form': form
				}
				return render(request, 'create_user.html', ctx)
		else:
			messages.error(
				request, 'Ocurrió un problema al crear usuario, por favor revise los datos ingresados')
			grupos = Group.objects.all()
			ctx = {
				'form': form,
				'grupos': grupos
			}
			return render(request, 'create_user.html', ctx)
		return redirect('users:users_list')
	form = SignUpForm()
	groups_list = Group.objects.all()
	ctx = {
		'groups_list': groups_list,
		'form': form
	}
	return render(request, 'create_user.html', ctx)


@login_required()
@transaction.atomic
def edit_user(request, pk):
	if request.POST:
		with transaction.atomic():
			try:
				us = User.objects.get(pk = request.POST['user_id'])
				us.first_name = request.POST['first_name']
				us.last_name = request.POST['last_name']
				us.is_active = request.POST['is_active']
				us.save()
				us.groups.clear()

				for x in request.POST.getlist('grupos'):
					g = Group.objects.get(id=x)
					g.user_set.add(us)
				messages.success(request, 'Usuario editado con éxito')
			except Exception as e:
				print (e)
				messages.error(request, 'Ocurrió un problema al editar usuario')
		return redirect('users:users_list')
	else:
		try:
			user = User.objects.get(pk = pk)
		except Exception as e:
			print (e)
		groups_list = Group.objects.all()

		ctx ={
			'groups_list':groups_list,
			'user':user,
		}
		return render(request, 'edit_user.html', ctx )

 

#  Passwords
@login_required()
@transaction.atomic
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Contraseña actualizada correctamente')
			return redirect('generals:index')
		else:
			messages.error(request, 'No se pudo actualizar contraseña')

			return render(request, 'change_password.html', {'form': form})
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {'form': form})

# Groups
@login_required()
@transaction.atomic
def groups_list(request):
	groups_list = Group.objects.all()
	ctx = {
		'groups_list': groups_list,
	}
	return render(request, 'groups_list.html', ctx )

@login_required()
@transaction.atomic
def create_group(request):
	if request.POST:
		with transaction.atomic():
			try:
				gp = Group()
				gp.name = request.POST['name'][:80]
				gp.save()

				for x in request.POST.getlist('permissions'):
					per = Permission.objects.get(id = x)
					gp.permissions.add(per)

				messages.success(request, 'Grupo creado con éxito')
			except Exception as e:
				print (e)
				messages.error(request, 'Ocurrió un problema al crear grupo')
		return redirect('users:groups_list')
	else:
		permissions_list = Permission.objects.all().order_by('-content_type')
		
		# TODO
		# Este todo sirve para saber si los permisos son filtrados por tipo de modelo
		# content_type = ContentType.objects.get_for_model(Company)
		# all_permissions = Permission.objects.filter(content_type=content_type)

		ctx = {
			'permissions_list':permissions_list,
		}
		return render(request, 'create_group.html', ctx )

@login_required()
@transaction.atomic
def edit_group(request, pk):
	if request.POST:
		with transaction.atomic():
			try:
				gp = Group.objects.get(pk = request.POST['id'])
				gp.name = request.POST['name'][:80]
				gp.save()
				gp.permissions.clear()
				for x in request.POST.getlist('permissions'):
					per = Permission.objects.get(id = x)
					gp.permissions.add(per)
				messages.success(request, 'Grupo editado con éxito')
			except Exception as e:
				print (e)
				messages.error(request, 'Ocurrió un problema al editar grupo')
		return redirect('users:groups_list')
	else:
		gp = Group.objects.get(pk = pk)
		groups_list = Permission.objects.all().order_by('-content_type')
		ctx = {
			'groups_list':groups_list,
			'gp':gp
		}
		return render(request, 'edit_group.html', ctx )




