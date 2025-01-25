from django import template


register = template.Library()

@register.filter
def format_milliers(value):
    try:
        return f"{value:,.0f} FG".replace(',', ' ').replace('.', ',')
    except (ValueError, TypeError):
        return value

