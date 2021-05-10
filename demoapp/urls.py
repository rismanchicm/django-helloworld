from django.urls import path, re_path

from . import views

app_name = 'demoapp'
urlpatterns = [
    path('', views.app_home, name='app_home'),
    #Using function view same result as CompanyListView CBV
    #path('company/', views.company_list, name='company_list'),
    # Using Class Based View
    path('company/', views.CompanyView.as_view(), name='company_list'),
    # Using generic Class Based View
    #path('company/', views.CompanyListView.as_view(), name='company_list'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('company/<int:pk>/update', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/delete', views.CompanyDeleteView.as_view(), name='company_delete'),
    #Employee URL's
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='employee_delete'),

]