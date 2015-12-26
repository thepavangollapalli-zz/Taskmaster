from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name="login"),
    url(r'^index/', views.Index.as_view(), name="index"),
    url(r'^add/', views.AddView.as_view(), name="add"),
    url(r'^update/', views.update, name="update"),
    url(r'^edit/', views.editView, name="edit"),
    url(r'^delete/', views.delete, name="delete"),
    url(r'^login/', views.LoginView.as_view(), name="login")
]