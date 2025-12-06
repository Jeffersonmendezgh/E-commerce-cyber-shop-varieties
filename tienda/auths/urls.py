from django.urls import path
from . import views #PARA importar los modelos

app_name = "auths"

urlpatterns = [
    path("register/", views.signing_view, name="signing"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
   # path("activate_account/<uidb64>/<token>/", views.verify_account, name="activate_account"),
    path("activate_account/<uidb64>/<token>/", views.activate_account, name="activate_account"),
]