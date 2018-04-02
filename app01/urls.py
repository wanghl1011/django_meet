
from django.conf.urls import url,include
from app01 import views
urlpatterns = [
    url(r'^show/$',views.show_meeting_room),
    url(r'^login/$',views.login),
    url(r'^order/$',views.order),
    url(r'^select/$',views.select),
]