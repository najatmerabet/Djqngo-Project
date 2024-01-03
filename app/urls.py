from django.urls.resolvers import settings
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import loginForm
from .forms import MyPasswordResetForm

urlpatterns = [
    path('', views.home),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('category/<slug:val>',views.CategoryView.as_view(),name="category"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(),name="Productdetail"),
    path('category-title/<val>',views.CategoryTitle.as_view(), name="CategoryTitle"),
    path('registration/',views.CustomerRegistration.as_view(),name="registration"),
    path('accounts/login',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=loginForm),name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_resset.html',form_class=MyPasswordResetForm),name='password_resset'),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('address',views.address,name="address"),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
