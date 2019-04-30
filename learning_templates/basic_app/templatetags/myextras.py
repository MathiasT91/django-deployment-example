from django import template

register = template.Library()

def cutfn(value, arg):
    """
    This cuts out all values of arg from the string
    """

    return value.replace(arg,'')

register.filter('cutting',cutfn)
