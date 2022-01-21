from django.contrib import admin
from django.urls import path,include
from User_Login import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("User_Login.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send-form-email', views.SendFormEmail.as_view(), name='send_email'),
]
