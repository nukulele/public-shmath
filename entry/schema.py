import graphene
from graphene_django import DjangoObjectType

from .models import Tag, Entry


def _get_page( kwargs ):
    page = kwargs['page']
    paginateBy = kwargs.get( 'paginateBy', 50 )
    first = (page - 1) * paginateBy
    last = first + paginateBy
    return [first, last]


class TagType( DjangoObjectType ):
    class Meta:
        model = Tag


class EntryType( DjangoObjectType ):
    class Meta:
        model = Entry


class Query( graphene.ObjectType ):
    entries = graphene.List( EntryType,
                             page=graphene.Int(),
                             paginateBy=graphene.Int(),
                             tag=graphene.String(),
                             ordering=graphene.String(),
                             )

    tags = graphene.List( TagType,
                          page=graphene.Int(),
                          paginateBy=graphene.Int(),
                          )

    entry = graphene.Field( EntryType,
                            slug=graphene.String(),
                            name=graphene.String()
                            )

    tag = graphene.Field( TagType,
                          slug=graphene.String(),
                          name=graphene.String()
                          )

    entry_count = graphene.Int( tag=graphene.String(), )
    tag_count = graphene.Int()

    def resolve_entries( self, info, **kwargs ):
        qs = Entry.objects.all()
        if "ordering" in kwargs:
            qs = qs.order_by( kwargs['ordering'] )
        if "tag" in kwargs:
            qs = qs.filter( tags__slug=kwargs["tag"] )
        if "page" in kwargs:
            first, last = _get_page( kwargs )
            qs = qs[first:last]
        return qs

    def resolve_tags( self, info, **kwargs ):
        qs = Tag.objects.all()
        if "page" in kwargs:
            first, last = _get_page( kwargs )
            qs = qs[first:last]
        return qs

    def resolve_entry( self, info, **kwargs ):
        slug = kwargs.get( 'slug' )
        name = kwargs.get( 'name' )
        if slug is not None:
            return Entry.objects.get( slug=slug )
        if name is not None:
            return Entry.objects.get( name=name )
        return None

    def resolve_tag( self, info, **kwargs ):
        slug = kwargs.get( 'slug' )
        name = kwargs.get( 'name' )
        if slug is not None:
            return Tag.objects.get( slug=slug )
        if name is not None:
            return Tag.objects.get( name=name )
        return None

    def resolve_tag_count( self, info, **kwargs ):
        return Tag.objects.count()

    def resolve_entry_count( self, info, **kwargs ):
        qs = Entry.objects.all()
        if "tag" in kwargs:
            qs = qs.filter( tags__slug=kwargs["tag"] )
        return qs.count()


schema = graphene.Schema( query=Query )
