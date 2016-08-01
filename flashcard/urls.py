from django.conf.urls import url
from . import views

app_name = 'flashcard'

urlpatterns = [
    # /
    url(r'^flashcard/?$',                            views.index,    name='index'),
    # /flashcard/create
    url(r'^flashcard/create/?$',                     views.create_set, name='create'),
    # /flashcard/112
    url(r'^flashcard/(?P<set_id>[0-9]+)(:show)?/?$', views.show_set, name='show'),
    # /flashcard/112:edit
    url(r'^flashcard/(?P<set_id>[0-9]+)/edit/?$',    views.edit_set, name='edit'),
    # /flashcard/112:save
    url(r'^flashcard/(?P<set_id>[0-9]+)/save/create=(?P<create>[0-9]+)/?$',  views.save_set, name='save'),
    # /flashcard/112/learn
    url(r'^flashcard/(?P<set_id>[0-9]+)/learn/?$', views.learn, name='learn'),
    # /flashcard/112/flip
    url(r'^flashcard/(?P<set_id>[0-9]+)/flip/?$', views.flip, name='flip'),
    # /flashcard/112/export
    url(r'^flashcard/(?P<set_id>[0-9]+)/export/?$', views.export, name='export'),
]