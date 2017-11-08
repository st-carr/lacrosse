# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Player(models.Model):
    """"
    Model representing a Player
    """

    height = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=200)
    number = models.PositiveSmallIntegerField()
    PLAYER_POSITION = (
        'Attack',
        'Defense',
        'Goalie',
        'Midfield',
        'Long Stick Midfield',
        'Attack/Midfield',
        'FaceOff',
    )
    position = models.CharField(max_length=30, choices=zip(PLAYER_POSITION, PLAYER_POSITION), blank=True, default='fr', help_text='Player Position')
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    
    USA_STATES = (
        'Alabama', 
        'Alaska',
        'Arizona',
        'Arkansas',
        'California', 
        'Colorado',
        'Connecticut', 
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois', 
        'Indiana',
        'Iowa',
        'Kansas', 
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi', 
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Carolina',
        'North Dakota',
        'Ohio',
        'Oklahoma', 
        'Oregon',
        'Pennsylvania', 
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont', 
        'Virginia',
        'Washington', 
        'West Virginia', 
        'Wisconsin',
        'Wyoming',
    )
    state = models.CharField(max_length=50, choices=zip(USA_STATES, USA_STATES), blank=True)
    weight = models.PositiveSmallIntegerField(null=True)
    PLAYER_YEAR = (
        'RedShirt',
        'Freshman',
        'Sophomore',
        'Junior',
        'Senior',
        'Graduate',
    )
    year = models.CharField(max_length=20, choices=zip(PLAYER_YEAR, PLAYER_YEAR), blank=True, default='fr', help_text='Player Class Standing')
    city = models.CharField(max_length=200)
    high_school = models.CharField(max_length=200)
    PUBLIC_PRIVATE = (
        'Private',
        'Public',
    )
    hs_type = models.CharField(max_length=10, choices=zip(PUBLIC_PRIVATE, PUBLIC_PRIVATE), blank=True, default='fr', help_text='Private or Public High School')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s | %s' % (self.school,self.name)

    class Meta:
        ordering = ['school', 'number']
        permissions = (
            ("can_edit_player", "Can edit player"),
        )

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('player-detail', args=[str(self.id)])


class School(models.Model):
    name = models.CharField(max_length=200)
    league = models.ForeignKey('League', on_delete=models.SET_NULL, null=True)
    roster_website = models.URLField(max_length=200, default='')
    slug = models.SlugField(max_length=50, default='')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class League(models.Model):
    name = models.CharField(max_length=200)
    division = models.ForeignKey('Division', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=50, default='')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Division(models.Model):
    NCAA_DIVISION = (
        ('d1', 'Division 1'),
        ('d2', 'Division 2'),
        ('d3', 'Division 3'),
    )
    name = models.CharField(max_length=2, choices=NCAA_DIVISION, blank=True, default='d1', help_text='NCAA Division')
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Data_Flag(models.Model):
    player_instance = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True)
    user_instance = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user_report = models.TextField(max_length=1000)

    class Meta:
        permissions = (("can_flag_player", "Flag player roster data."),)