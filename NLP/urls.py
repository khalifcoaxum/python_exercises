from django.conf.urls import url
from . import views
from NLP.views import save_user_data

urlpatterns = [
    url(r'^$', views.user_data, name='user_data'),
    url(r'^$', views.save_user_data),
]