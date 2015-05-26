__author__ = 'Stephen'

from django.conf.urls import url

from auditor_management import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^test/$', views.test, name='test')
]
