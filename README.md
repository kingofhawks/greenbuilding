greenbuilding
=============

绿色施工科研项目

** Installation

1. pip install -r requirements.txt

2. Auto create database table

> python manage.py makemigrations #to create migrations for those changes
> python manage.py migrate #to apply those changes to the database.

3. Disable Windows Firewall to let 8000 port remote reachable

4. Create backend super admin user

> python manage.py createsuperuser
> Username: admin
> Password: 11111

4. i18n support  
cd app_directory  
django-admin makemessages -l zh_CN  
django-admin compilemessages -l zh_CN  
4. python manage.py runserver 0.0.0.0:8000


Dependencies:
1.reportlab
under windows you need to run CMD as administrator：pip install reportlab
2.gettext for i18n  
http://www.gnu.org/software/gettext/  
https://mlocati.github.io/articles/gettext-iconv-windows.html  
3.phantomjs for PDF render  

