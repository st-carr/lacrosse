from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^m$', views.RostersView.as_view(), name='rosters'),
]

urlpatterns += [
    url(r'^m/(?P<division>[d][1-3])/$', views.DivisionView.as_view(), name='division-list'),
]

urlpatterns += [
    url(r'^m/(?P<division>[d][1-3])/(?P<league>[\w-]+)/$', views.LeagueView.as_view(), name='league-list'),
]

urlpatterns += [
    url(r'^m/(?P<division>[d][1-3])/(?P<league>[\w-]+)/(?P<school>[\w-]+)/$', views.SchoolView.as_view(), name='school-list'),
]

urlpatterns += [
    url(r'^flag-player/(?P<pk>[\d]+)/$', views.flag_player_data, name='flag-player'),
]

urlpatterns += [
    url(r'^edit-player/(?P<pk>[\d]+)/$', views.edit_player_data, name='edit-player'),
]

urlpatterns += [
    url(r'^add-player/(?P<pk_school>[\w-]+)/$', views.add_player_data, name='add-player'),
]

urlpatterns += [
    url(r'^delete-player/(?P<pk>[\d]+)/$', views.delete_player_data, name='delete-player'),
]