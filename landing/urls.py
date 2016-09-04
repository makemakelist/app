from django.conf.urls import url

from landing.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_page'),
]