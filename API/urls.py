
from django.contrib import admin
from django.urls import path
from vikas import views
urlpatterns = [
    path('admin/',views.admin),
    path('',views.index),
    path('admin/verify',views.verify),
    path('admin/add_user',views.add),
    path('admin/user_update',views.update),
    path('admin/delete_user',views.delete_user),
    path('admin/update_user',views.update_user)
]
