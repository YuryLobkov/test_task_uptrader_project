from django import template
from nested_menu.models import MenuItem
from django.utils.html import format_html

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    all_items = MenuItem.objects.all().select_related(
        'parent')  # every item in database
    for item in all_items:
        if item.name == menu_name:
            selected_menu = item

    output_html = f'<ul> <li> <a href="{selected_menu.url}">{selected_menu.name}</a>'
    output_html += draw_childs(selected_menu, all_items, current_url)
    output_html += ' </li> </ul>'
    return format_html(output_html)


def draw_childs(parent, all_items, current_url):
    # check if needed to unfold menu item
    if not current_url.startswith(parent.url): 
        return ''
    # render child element
    child_tree = '<ul>'
    for item in all_items:
        if item.parent == parent:
            if item.url == current_url:
                child_tree += f'<li class="Active" style="font-weight: bold"><a href="{item.url}">{item.name}</a>'
            else:
                child_tree += f'<li><a href="{item.url}">{item.name}</a>'                
            # if this element has childs, recursive render
            if check_childs(item, all_items):
                child_tree += draw_childs(item, all_items, current_url)
            child_tree += '</li>'
    child_tree += '</ul>'
    return child_tree

# check childs func to avoid additional db hits
def check_childs(item_to_check, all_items):
    for item in all_items:
        if item.parent == item_to_check:
            return True
    return False
