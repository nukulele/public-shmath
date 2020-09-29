from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify


class Tag( models.Model ):
    name = models.CharField( max_length=100, unique=True )
    slug = models.SlugField( max_length=100, blank=True, unique=True, primary_key=True )

    class Meta:
        ordering = [ 'slug' ]

    def clean( self ):
        self.slug = slugify( self.name )

    def __str__( self ):
        return self.slug


class Entry( models.Model ):
    name = models.CharField( max_length=100, unique=True )
    slug = models.SlugField( max_length=100, blank=True, unique=True, primary_key=True )
    text = models.TextField()
    date_create = models.DateTimeField( auto_now_add=True )
    date_edit = models.DateTimeField( auto_now=True )
    tags = models.ManyToManyField( Tag, blank=True )

    class Meta:
        ordering = [ 'slug' ]
        verbose_name_plural = "entries"

    def clean( self ):
        self.slug = slugify( self.name )

    def __str__( self ):
        return self.slug

    def get_absolute_url( self ):
        return reverse_lazy( "entry-detail", kwargs={ 'slug': self.slug } )
