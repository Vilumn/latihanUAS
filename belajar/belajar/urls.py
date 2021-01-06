"""belajar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from uas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('folder/', views.testing ,name='binatang1'),
    path('folder/create', views.FolderCreate.as_view() ,name='foldercreate'),
    path('folder/update/<int:pk>', views.FolderUpdate.as_view() ,name='folderupdate'),
    path('folder/delete/<int:pk>', views.FolderDelete.as_view() ,name='folderdelete'),

    path('folder1/<int:pk>', views.folder1, name='binatang2'),

]
