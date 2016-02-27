from django.conf.urls import url
from . import views

# assigns a view called post_list to ^$ URL. 
#This regular expression will match ^ (a beginning) followed by $ (an end) - 
#so only an empty string will match. In Django URL resolvers, '
#http://127.0.0.1:8000/' is not a part of the URL. 
#This pattern will tell Django that views.post_list is the right place 
#to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
