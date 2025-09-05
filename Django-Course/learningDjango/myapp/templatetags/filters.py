#Creamos filtros para nuestro template
from django import template

register = template.Library()

@register.filter(name='greeting')
def greeting(value):
    long = ''
    if len(value) >= 8:
        long = "<p>Your name is large</p>"
    return f"<h1 style='background:green;color:white;'>Welcome, {value}</h1> {long}"
