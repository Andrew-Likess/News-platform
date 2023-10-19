from django.urls import path, include
from users.views import Register
from .views import CustomLoginView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('users/login/', CustomLoginView.as_view(), name='login'),

]
