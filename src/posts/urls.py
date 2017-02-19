from django.conf.urls import url

from . import views as pv

urlpatterns = [
    url(r'^$',pv.post_list,name="list"),
    url(r'^create',pv.post_create),
    url(r'^(?P<slug>[\w-]+)/edit/$',pv.post_update),
    url(r'^(?P<slug>[\w-]+)/$',pv.post_retrieve,name="detail"),
    url(r'^(?P<slug>[\w-]+)/delete',pv.post_delete),
]
