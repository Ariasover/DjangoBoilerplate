# Django imports
from django.urls import path

# Local imports
from apps.users import views as users_views
 
app_name = 'users'

urlpatterns = [
    #User's URL
    path('users-list/', users_views.users_list, name='users_list'),    
    # url(r'^listado-usuarios/$', views.listado_usuarios, name='listado_usuarios'),
    # url(r'^crear-usuario/$', views.crear_usuario, name='crear_usuario'),
    # url(r'^editar-usuario/(?P<codigo>\d+)/$', views.editar_usuario, name='editar_usuario'),
    # path('cambiar-password/', views.change_password, name='change_password'),
    # #url(r'^activate/(?P<uidb64>.+)/(?P<token>.+)/$',views.activate, name='activate'),
    # url(r'^listado-grupos/$', views.listado_grupos, name='listado_grupos'),
    # url(r'^crear-grupo/$', views.crear_grupo, name='crear_grupo'),
    # url(r'^editar-grupo/(?P<codigo>\d+)/$', views.editar_grupo, name='editar_grupo'),
]