# Django imports
from django.urls import path

# Local imports
from apps.generals import views as general_views


app_name = 'generals'
urlpatterns = [
    path('', general_views.login, name='login'),    
    path('index/', general_views.index, name='index'),    
    path('logout-user/', general_views.logout_user, name='logout_user'),    
]
