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
    url(r'^flag-player/(?P<pk>[\d]+)/$', views.FlagPlayerDetailView.as_view(), name='flag-player'),
]