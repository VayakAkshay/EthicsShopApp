from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('login/',views.Loginpage,name="Loginpage"),
    path('signup/',views.Signuppage,name="Signuppage"),
    path('forget-pass/',views.ForgetPage,name="ForgetPage"),
    path('password/',views.PasswordPage,name="PasswordPage"),
    path("change-pass/",views.ChangePassPage,name="ChangePassPage"),
    path('new_pass/',views.new_pass,name="new_pass"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)