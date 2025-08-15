from django import template

register = template.Library()

@register.filter
def lookup(dictionary, key):
    """
    Custom template filter to lookup dictionary values by key
    Usage: {{ dict|lookup:key }}
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key, 0)
    return 0

@register.filter
def multiply(value, arg):
    """
    Multiplies the value by the argument
    Usage: {{ value|multiply:2 }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0