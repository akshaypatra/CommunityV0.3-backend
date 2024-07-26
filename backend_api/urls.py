from django.urls import path, include
from .views import UserCreateView,UserDetailView
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('api-token-auth/', drf_views.obtain_auth_token),
]

# Registration: POST to /api/register/ with user data to register a new user.
# POST request to /api/api-token-auth/ with username and password.
