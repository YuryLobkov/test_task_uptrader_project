from django import template
from nested_menu.models import MenuItem
from django.utils.html import format_html

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(
        parent__isnull=True, name=menu_name).prefetch_related('children') # getting root item (menu name)
    menu_html = recursive_draw(menu_items, current_url)
    return format_html(menu_html)


def recursive_draw(items, current_url, selected=False):
    menu_html = '<ul>'
    for item in items:
        if current_url.startswith(item.url): # check if selected item is child of this item (or is selected itself)
            selected = True
        if item.is_active(current_url): # if current url is url in current item, set css class "active"
            active_class = 'active'
        else:
            active_class = ''
        menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a>'
        children = item.children.all() # get all childrens of current item to further render
        if children and selected: # check if there are childrens and if they are 1st level nested (to satisfy task point #2)
            menu_html += recursive_draw(children, current_url)
            selected = False # drop selected flag not to render non-related items with selected item
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
