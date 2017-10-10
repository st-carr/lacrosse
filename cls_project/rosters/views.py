from django.shortcuts import render
from .models import Player, School, Division, League, Data_Flag
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import FlagPlayerForm
# Create your views here.

class FlagPlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player
    template_name = 'rosters/flag_player.html'

    
    def get_context_data(self, **kwargs):
        context = super(FlagPlayerDetailView, self).get_context_data(**kwargs)
        context['player_list'] = Player.objects.get(id=self.kwargs['pk'])
        context['form'] = FlagPlayerForm()
        return context 
    


class SchoolView(generic.ListView):
    model = School
    template_name = 'rosters/school.html'


    def get_context_data(self, **kwargs):
        context = super(SchoolView, self).get_context_data(**kwargs)
        context['division_list'] = Division.objects.all()
        context['league_list'] = League.objects.all()
        context['player_list'] = Player.objects.filter(school__slug = self.kwargs['school'])
        context['this_school'] = School.objects.get(slug = self.kwargs['school'])
        # And so on for more models
        return context

class LeagueView(generic.ListView):
    model = League
    template_name = 'rosters/league.html'

    def get_context_data(self, **kwargs):
        context = super(LeagueView, self).get_context_data(**kwargs)
        context['division_list'] = Division.objects.all()
        context['this_league'] = League.objects.get(slug = self.kwargs['league'])
        context['school_list'] = School.objects.filter(league__slug = self.kwargs['league'])
        context['player_list'] = Player.objects.filter(school__league__slug = self.kwargs['league'])
        # And so on for more models
        return context


class DivisionView(generic.ListView):
    model = Division
    template_name = 'rosters/division.html'

    def get_context_data(self, **kwargs):
        context = super(DivisionView, self).get_context_data(**kwargs)
        context['league_list'] = League.objects.all()
        context['school_list'] = School.objects.all()
        context['player_list'] = Player.objects.filter(school__league__division__name = self.kwargs['division'])
        # And so on for more models
        return context

  
class RostersView(generic.ListView):
    context_object_name = 'player_list'
    template_name = 'rosters/rosters.html'
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(RostersView, self).get_context_data(**kwargs)
        context['division_list'] = Division.objects.all()
        context['league_list'] = League.objects.all()
        context['school_list'] = School.objects.all()
        # And so on for more models
        return context


def index(request):
    #View function for home page of site. 

    
    # Generate counts of some of the main objects
    num_players = Player.objects.all().count()
    # Available books (status = 'a')
    num_players_atk = Player.objects.filter(position__exact='atk').count()
    num_players_def = Player.objects.filter(position__exact='def').count()
    num_players_gl = Player.objects.filter(position__exact='gl').count()
    num_players_fo = Player.objects.filter(position__exact='fo').count()
    num_players_mid = Player.objects.filter(position__exact='mid').count()
    num_players_lsm = Player.objects.filter(position__exact='lsm').count()

    num_players_brown = Player.objects.filter(school__name__icontains='Brown University').count()
    num_players_harvard = Player.objects.filter(school__name__icontains='Harvard University').count()
    num_players_yale = Player.objects.filter(school__name__icontains='Yale University').count()


    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_players':num_players, 'num_players_atk':num_players_atk, 'num_players_def':num_players_def, 'num_players_gl':num_players_gl, 'num_players_fo':num_players_fo,
        'num_players_mid':num_players_mid, 'num_players_lsm':num_players_lsm, 'num_players_brown':num_players_brown,
        'num_players_harvard':num_players_harvard, 'num_players_yale':num_players_yale, 'num_visits':num_visits},
    )
