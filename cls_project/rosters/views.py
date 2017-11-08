from django.shortcuts import render
from .models import Player, School, Division, League, Data_Flag
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import FlagPlayerForm, EditPlayerForm, AddPlayerForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages 
# Create your views here.

@permission_required('rosters.can_edit_player')
def delete_player_data(request, pk):
    """
    View function for flagging player data as incorrect
    """
    # If this is a POST request then process the Form data
    player_list = Player.objects.get(id=pk)
    this_school = School.objects.get(name=player_list.school)
    if request.method == 'POST':
        # redirect to a new URL:
        playerDivision = Division.objects.get(league__school__name=player_list.school)
        playerLeague = League.objects.get(school__name=player_list.school)
        playerSchool = this_school.slug
        deletePlayer = Player.objects.filter(id=pk)
        deletePlayer.delete()
        messages.success(request, 'Player data successfully deleted.')
        return HttpResponseRedirect(reverse('school-list', kwargs={'division':playerDivision,'league':playerLeague,'school':playerSchool}))






    return render(request, 'rosters/delete_player.html', {'player_list':player_list})





@permission_required('rosters.can_edit_player')
def add_player_data(request, pk_school):
    """
    View function for flagging player data as incorrect
    """
    # If this is a POST request then process the Form data
    
    this_school = School.objects.get(slug=pk_school)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = AddPlayerForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            playerDivision = Division.objects.get(league__school__slug=pk_school)
            playerLeague = League.objects.get(school__slug=pk_school)
            playerSchool = this_school.slug
            newPlayerData = Player(
                number = form.cleaned_data['number'],
                school = this_school,
                name = form.cleaned_data['name'],
                year = form.cleaned_data['year'],
                state = form.cleaned_data['state'],
                position = form.cleaned_data['position'],
                height = form.cleaned_data['height'],
                weight = form.cleaned_data['weight'],
                city = form.cleaned_data['city'],
                high_school = form.cleaned_data['high_school'],
                hs_type = form.cleaned_data['hs_type']
            )
            newPlayerData.save()
            #success message
            messages.success(request, 'Player data successfully updated.')
           # redirect to a new URL:
            return HttpResponseRedirect(reverse('school-list', kwargs={'division':playerDivision,'league':playerLeague,'school':playerSchool}))
        else:
            return HttpResponseRedirect(reverse('index'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = AddPlayerForm()
    
    return render(request, 'rosters/add_player.html', {'form': form, 'this_school':this_school})

@permission_required('rosters.can_edit_player')
def edit_player_data(request, pk):
    """
    View function for flagging player data as incorrect
    """
    # If this is a POST request then process the Form data
    player_list = Player.objects.get(id=pk)
    this_school = School.objects.get(name=player_list.school)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = EditPlayerForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            playerEdit = Player.objects.get(id=pk)
            playerEdit.number = form.cleaned_data['number']
            playerEdit.name = form.cleaned_data['name']
            playerEdit.year = form.cleaned_data['year']
            playerEdit.state = form.cleaned_data['state']
            playerEdit.position = form.cleaned_data['position']
            playerEdit.height = form.cleaned_data['height']
            playerEdit.weight = form.cleaned_data['weight']
            playerEdit.city = form.cleaned_data['city']
            playerEdit.high_school = form.cleaned_data['high_school']
            playerEdit.hs_type = form.cleaned_data['hs_type']
            playerEdit.save()
           
            #success message
            messages.success(request, 'Player data successfully updated.')
            # redirect to a new URL:
            playerDivision = Division.objects.get(league__school__name=player_list.school)
            playerLeague = League.objects.get(school__name=player_list.school)
            playerSchool = this_school.slug
            return HttpResponseRedirect(reverse('school-list', kwargs={'division':playerDivision,'league':playerLeague,'school':playerSchool}))

    # If this is a GET (or any other method) create the default form.
    else:
        editFormData = {'number':player_list.number, 'name':player_list.name, 'height':player_list.height, 'weight':player_list.weight,
         'position':player_list.position, 'state':player_list.state, 'year':player_list.year, 'high_school':player_list.high_school, 
         'hs_type':player_list.hs_type, 'city':player_list.city}
        form = EditPlayerForm(initial=editFormData)
    
    return render(request, 'rosters/edit_player.html', {'form': form, 'player_list':player_list, 'this_school':this_school})

@login_required
def flag_player_data(request, pk):
    """
    View function for flagging player data as incorrect
    """
    player_list = Player.objects.get(id=pk)
    this_school = School.objects.get(name=player_list.school)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = FlagPlayerForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            newPlayerDataFlag = Data_Flag(user_report=form.cleaned_data['user_report'], player_instance=Player.objects.get(id=pk), user_instance=request.user)
            newPlayerDataFlag.save()

            #success message
            messages.success(request, 'Report successfully submitted.')
            # redirect to a new URL:
            playerDivision = Division.objects.get(league__school__name=player_list.school)
            playerLeague = League.objects.get(school__name=player_list.school)
            playerSchool = this_school.slug
            return HttpResponseRedirect(reverse('school-list', kwargs={'division':playerDivision,'league':playerLeague,'school':playerSchool}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = FlagPlayerForm()

    
    return render(request, 'rosters/flag_player.html', {'form': form, 'player_list':player_list})





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
