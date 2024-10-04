"""
URL configuration for ramen_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from mypage import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('747947/', admin.site.urls),
    path('', views.home, name='home'),
    path('hokkaido/', views.hokkaido, name='hokkaido'),
    path('tohoku/', views.tohoku, name='tohoku'),
    path('kanto/', views.kanto, name='kanto'),
    path('tyubu/', views.tyubu, name='tyubu'),
    path('kinki/', views.kinki, name='kinki'),
    path('tyugoku/', views.tyugoku, name='tyugoku'),
    path('shikoku/', views.shikoku, name='shikoku'),
    path('kyusyu/', views.kyusyu, name='kyusyu'),
    path('profile', views.profile, name='profile'),
    path('wakayama/', views.wakayama, name='wakayama'),
    path('osaka/', views.osaka, name='osaka'),


    path('comments/', views.comment_list, name='comment_list'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'), 
    path('store/<int:store_id>/', views.store_detail, name='store_detail'),
    path('image_form/', views.upload_store, name='image_upload'),

    path('shimasyo/<int:page>/', views.shimasyo, name='shimasyo'),
    path('seino/<int:page>/', views.seino, name='seino'),
    path('ramenhayato/<int:page>/', views.ramenhayato, name='ramenhayato'),
    path('kadoya/<int:page>/', views.kadoya, name='kadoya'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

