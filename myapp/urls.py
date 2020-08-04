from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns = [
    path('trial',views.trial,name='trial'),
    path('profile',views.profile,name='profile'),
]
