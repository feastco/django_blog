"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from posting.views import *
from django.conf.urls.static import static
from posting import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>/', views.PostingView.as_view(), name='detail'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('update_post/<int:pk>/', views.UpdatePost.as_view(), name='update_post'),
    path('detail/<int:pk>/delete', views.DeletePost.as_view(), name='delete_post'),
    path('search/', views.SearchPosting.as_view(), name='search_post'),
    path('contact/', views.contact_us, name='contact_us'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
