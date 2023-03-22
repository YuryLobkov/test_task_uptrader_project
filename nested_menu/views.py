from django.shortcuts import render

# item_page views for rendering ierarchical urls up to 3 levels
def item_page(request, item_name):
    context = {'pagename': item_name}
    return render(request, 'index.html', context=context)


def item_page_level2(request, item_name, item_name2):
    context = {'pagename': item_name, 'item_name2': item_name2}
    return render(request, 'index.html', context=context)


def item_page_level3(request, item_name, item_name2, item_name3):
    context = {'pagename': item_name, 'item_name2': item_name2, 'item_name3': item_name3}
    return render(request, 'index.html', context=context)


def homepage(request):
    return render(request, 'index.html')
