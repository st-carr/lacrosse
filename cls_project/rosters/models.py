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
        ('atk', 'Attack'),
        ('def', 'Defense'),
        ('gl', 'Goalie'),
        ('mid', 'Midfield'),
        ('lsm', 'Long Stick Midfield'),
        ('am', 'Attack/Midfield'),
        ('fo', 'FaceOff'),
    )
    position = models.CharField(max_length=3, choices=PLAYER_POSITION, blank=True, default='fr', help_text='Player Position')
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=200)
    weight = models.PositiveSmallIntegerField(null=True)
    PLAYER_YEAR = (
        ('rs', 'RedShirt'),
        ('fr', 'Freshman'),
        ('so', 'Sophomore'),
        ('jr', 'Junior'),
        ('sr', 'Senior'),
        ('gr', 'Graduate'),
    )
    year = models.CharField(max_length=2, choices=PLAYER_YEAR, blank=True, default='fr', help_text='Player Class Standing')
    city = models.CharField(max_length=200)
    high_school = models.CharField(max_length=200)
    PUBLIC_PRIVATE = (
        ('Private', 'Private'),
        ('Public', 'Public'),
    )
    hs_type = models.CharField(max_length=10, choices=PUBLIC_PRIVATE, blank=True, default='fr', help_text='Private or Public High School')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s | %s' % (self.school,self.name)

    class Meta:
        ordering = ['school', 'number']

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