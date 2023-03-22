from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<item_name>', views.item_page, name='level1_page'),
    path('<item_name>/<item_name2>', views.item_page_level2, name='level2_page'),
    path('<item_name>/<item_name2>/<item_name3>', views.item_page_level3, name='level3_page'),
]