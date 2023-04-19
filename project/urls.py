"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from app import views
from . import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView,LoginView
from app.views import  admin_dashboard_view, admin_404,admin_contact_view,upload_picture, view_pictures,admin_password_reset

urlpatterns = [
    
    path('', views.index , name='index'),
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='admin/login.html'),name='adminlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin-dashboard', admin_dashboard_view, name='admin-dashboard'),
    path('admin/404', admin_404),
    path('admin-contact' ,admin_contact_view , name='admin-contact' ),
    path('admin-edit-contact/<int:contact_id>/', views.admin_edit_contact, name='admin-edit-contact'),
    path('admin-delete-contact/<int:contact_id>/', views.admin_delete_contact, name='admin-delete-contact'),
    path('upload-picture', upload_picture, name='upload_picture'),
    path('view-pictures/', view_pictures, name='view_pictures'),
    path('admin/password/reset/', admin_password_reset, name='admin_password_reset'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)