from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", views.SignupAPIView, name="signup"),
    path("login/", views.LoginAPIView, name="login"),
    path("<str:username>/", views.ProfileAPIView, name="profile"),
]
