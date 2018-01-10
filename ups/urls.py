from django.urls import path


from . import views

app_name = 'ups'
urlpatterns = [
	#upstable
    path('', views.index, name='index'),
	#batterytable
    path('battery/',views.batteries, name='batteries'),
	#upsedit
    path('edit/<int:id_s>/', views.ups_edit, name='ups_edit'),
    path('remove/<int:id_s>', views.ups_remove, name='ups_remove'),
	#batedit
    path('battery/edit/<str:id_s>/', views.bat_edit, name='bat_edit'),
    path('battery/remove/<str:id_s>', views.bat_remove, name='bat_remove'),    
       #newups
    path('new/', views.upsnew, name='upsnew'),
        #newbattery
    path('battery/new/', views.batnew, name='batnew'),
        #upssearch
    path('search/', views.get_ups_list, name='get_ups_list'),
        #batterysearch
    path('battery/search/', views.get_battery_list, name='get_battery_list')
    
]

