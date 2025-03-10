from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import RedirectView

from users import views as user_views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("food/", include("food.urls")),
    path("", RedirectView.as_view(url="/food/")),
    path("users/", include("users.urls")),
    ## Register, Login, Logout
    path("register/", user_views.register, name="register"),
    path("login/", authentication_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', authentication_views.LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    ## Profile
    path("profile/", user_views.profilepage, name="profile")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
