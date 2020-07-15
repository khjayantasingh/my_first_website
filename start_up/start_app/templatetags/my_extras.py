from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    #replace all arg in the string with the space
    return value.replace(value, ' ')

#register.filter('cut', cut)