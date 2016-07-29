from django import template

register = template.Library()


@register.filter
def at(lst, indx):
    return lst[indx]
