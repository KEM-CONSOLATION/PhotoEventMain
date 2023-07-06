from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('checkout/', views.initiate_payment, name='checkout'),
    path('login/',views.loginPage,name="login"),
    path('account_settings/', views.edit, name="account_settings"),
    path('logout/', views.logoutUser, name="logout" ),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),
    path('event/', views.event, name='event'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)