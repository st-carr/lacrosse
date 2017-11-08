import os

# django project name is adleads, replace adleads with your project name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cls_project.settings")

from .models import Player

player_list = Player.objects.all()

for player in player_list:
    if player.position == 'atk':
        player.position = 'Attack'
    elif player.position == 'gl':
        player.position = 'Goalie'
    elif player.position == 'mid':
        player.position = 'Midfield'
    elif player.position == 'def':
        player.position = 'Defense'
    elif player.position == 'lsm':
        player.position = 'Long Stick Midfield'
    elif player.position == 'fo':
        player.position = 'FaceOff'

