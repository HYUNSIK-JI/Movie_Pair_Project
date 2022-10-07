from django.contrib import admin
from django.urls import path
from . import views

app_name="Reviews"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>', views.detail, name="detail"),
    path('<int:pk>/delete', views.delete , name="delete"),
    path('<int:pk>/update', views.update, name="update"), 
]
