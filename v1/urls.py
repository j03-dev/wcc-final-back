from django.urls import path
from rest_framework.authtoken import views
from v1.views import UserView, ClotheView


urlpatterns = [
    path("user", UserView.as_view()),
    path("user/login", views.obtain_auth_token),
    path("clothes", ClotheView.as_view())
]
