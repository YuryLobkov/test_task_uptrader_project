from django import template
from nested_menu.models import MenuItem
from django.utils.html import format_html

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(
        parent__isnull=True, name=menu_name).prefetch_related('children')
    menu_html = recursive_draw(menu_items, current_url)
    return format_html(menu_html)


def recursive_draw(items, current_url, selected=False):
    menu_html = '<ul>'
    for item in items:
        if item.url in current_url:
            selected = True
        if item.is_active(current_url):
            active_class = 'active'
            selected = True
        else:
            active_class = ''
        menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a>'
        children = item.children.all()
        if children and selected:
            menu_html += recursive_draw(children, current_url)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
