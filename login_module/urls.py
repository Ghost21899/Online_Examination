from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

  
urlpatterns = [ 
    path('register', user_register, name = 'register'), 
    path('success', success, name = 'success'), 
    path('login', user_login, name = 'login'), 
    path('imgreg', user_registration_image, name='imgreg'), 
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 