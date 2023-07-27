from django.urls import path

from. import views

urlpatterns = [

    path('', views.api_view, name='api'),
    path('bdns/', views.bdns_filter_id, name='bdns_id'),
    path('locations/', views.get_locations, name='locations'),
    path('subsidloc/<str:location>/<str:loc_name>/', views.subsidies_location, name='subsidloc'),
    path('bdns_like/<str:bdns>/', views.subsidies_bdns_like, name='bdns_like'),
    path('bdns_location/<str:bdns>/<str:location>/<str:loc_name>/', views.subsidies_bdns_like_location, name='bdns_location'),
    path('title_like/<str:title>/', views.subsidies_title_like, name='title_like'),
    path('subsidy/budget/<str:budget>/', views.subsidies_budget_like, name='budget'),
    path('', views.api_view, name='api_view'),

]
