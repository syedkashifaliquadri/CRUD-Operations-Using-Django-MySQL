"""crud_app_SQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crudapplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp',views.emp, name='employee_insert'),
    path('show',views.show,name='employee_list'),
    path('edit/<int:id>',views.edit, name= 'employee_update'),
    # path('update/<int:id>',views.update, name= 'employee_update'),
    path('delete/<int:id>',views.delete,name= 'employee_delete'),
]
