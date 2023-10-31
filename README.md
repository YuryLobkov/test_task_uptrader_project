# test_task_uptrader_project
Tree menu test task for UpTrader

This repo already includes examlpe DB.
To run demo simple enough to run 'py manage.py runserver'. Default superuser login credentials are admin/admin.

To configure your own menu:
1. Delete existing db
2. Run 'py manage.py migrate'
3. Run 'py manage.py createsuperuser' and follow cl instructions
4. Go to 'localhost/admin', log in and add your menu items.
5. Edit index.html file, include your custom menu names as shown {% draw_menu 'your_menu_name'%}
