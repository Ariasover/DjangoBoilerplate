# Django imports
from django.urls import path

# Local imports
from apps.users import views as users_views
 
app_name = 'users'

urlpatterns = [
    # User's URLS
    path('users-list/', users_views.users_list, name='users_list'),    
    path('create-user/', users_views.create_user, name='create_user'),
    path('edit-user/<int:pk>/', users_views.edit_user, name='edit_user'),

    # Groups URLS
    path('groups-list/', users_views.groups_list, name='groups_list'),
    path('create-group/', users_views.create_group, name='create_group'),
    path('edit-group/<int:pk>/', users_views.edit_group, name='edit_group'),

    # Password's URLS
    path('change-password/', users_views.change_password, name='change_password'),

    # Activation URLS
        #path('activate/(?P<uidb64>.+)/(?P<token>.+)/$',views.activate, name='activate'),



]