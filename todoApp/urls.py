from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('note/<int:id>/',note),
    path('add/',add),
    path('delete/<int:id>/',delete),
    path('signup/',signup),
    path('login/',loginpage,name='login'),
    path('logout/',logout_user)

]