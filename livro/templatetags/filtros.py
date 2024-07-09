from django import template
from datetime import datetime

register = template.Library()

@register.filter
def mostrar_duracao(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        return f"{(value1 - value2).days} dias."
    
    return "Ainda não foi devolvido."