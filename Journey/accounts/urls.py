from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('to_get', views.to_get, name='to_get'),
    path('to_update/<int:pk>', views.to_update, name='to_update'),
    path('to_delete/<int:pk>',views.to_delete,name='to_delete'),
    path('login', views.login,name='login'),
    path('success', views.success, name='success'),
    # path('logout',views.logout,name='logout'),
]