from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", views.SignupAPIView.as_view(), name="signup"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("<str:username>/", views.ProfileAPIView.as_view(), name="profile"),
]
