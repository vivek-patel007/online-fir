from django.contrib import admin
from django.urls import path
from userfir import views


urlpatterns = [
    path('wanted-info/', views.criminal_view,name='criminal_view'),
    path('criminal-info/<criminal_id>/', views.criminal_detail,name='criminal_detail'),
    path('missing-person/', views.missing_person,name='missing_person'),
    path('person-detail/<missing_id>/', views.person_detail,name='person_detail'),
    path('edit-profile/', views.edit_profile,name='edit_profile'),
    path('edit-profile-police/', views.edit_profile_police,name='edit_profile_police'),
    path('search/', views.search,name='search_view'),
    path('create-fir/', views.create_fir,name='create_fir'),
    path('view-fir/', views.view_fir, name='view_fir'),
    path('approve-fir/<fir_id>', views.approve_fir,name='approve_fir'),
    path('change-password/', views.change_password,name='change_password'),
    path('forget-password/', views.forget_password,name='forget_password'),

]
