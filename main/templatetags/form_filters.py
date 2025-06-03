from django import template
register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    try:
        return field.as_widget(attrs={"class": css_class})
    except AttributeError:
        return field  # fallback nếu field không có .as_widget


@register.filter
def progress_percent(current, goal):
    try:
        return round((current / goal) * 100)
    except (ZeroDivisionError, TypeError):
        return 0