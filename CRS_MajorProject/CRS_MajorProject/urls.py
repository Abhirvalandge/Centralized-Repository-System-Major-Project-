"""CRS_MajorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from crs_App import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.crs_home_view),

    path('gov_schemes/',views.gov_schemes_view,name='gov_schemes'),
    path('education_s_list/',views.education_list_view,name='education_s_list'),
    path('health_s_list/',views.health_list_view,name='health_s_list'),
    path('agriculture_s_list/',views.agriculture_list_view,name='agriculture_s_list'),
    path('electricity_s_list/',views.electricity_list_view,name='electricity_s_list'),
    path('business_s_list/',views.business_list_view,name='business_s_list'),
    path('youth_s_list/',views.youth_list_view,name='youth_s_list'),

    path('gov_jobs_list/',views.gov_jobs_list_view,name='gov_jobs_list'),

    path('signup/', views.signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),
    path('contact_us/', views.contact_us, name="contact_us"),

    #Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


































    #path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.education_details_view, name='education_details'),
    #path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.health_details_view, name='health_details'),
    #path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.agriculture_details_view, name='agriculture_details'),
    #path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.electricity_details_view, name='electricity_details'),
    #path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.business_details_view, name='business_details'),
    #path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:post>/', views.youth_details_view, name='youth_details'),
