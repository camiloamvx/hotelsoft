"""hotelsoft1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^cliente/', include('apps.cliente.urls')),
    url(r'^alquiler/', include('apps.alquiler.urls')),
    url(r'^habitacion/', include('apps.habitacion.urls')),
    url(r'^usuario/', include('apps.usuarios.urls')),
    url(r'^$', LoginView.as_view(template_name = 'usuario/login.html'), name="login"),
    url(r'^reset/passwordReset/$', PasswordResetView.as_view(template_name = 'registration/password_reset_form.html', email_template_name = 'registration/password_reset_email.html'), name ="password_reset"),
    url(r'^reset/passwordResetDone', PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name="password_reset_confirm"),
    url(r'^reset/passwordResetComplete', PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name="password_reset_complete")
]