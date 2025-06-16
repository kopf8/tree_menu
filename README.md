# <u>Tree menu app (based on Python & Django)</u>

Multy-level menu, stored in database, editable via standard admin panel.
Rendered via template tag. By default, always expanded down to the current active menu.

## Requirements
- Python 3.9+  
- Django 5.2.1+  
- SQLite or any other database supported by Django

## Project setup & launch
Clone repository via SSH to your local machine:
```bash
git clone git@github.com:kopf8/tree_menu.git
```
   
Install project dependencies:
```bash
python -m venv .venv
source .venv/Scripts/activate # for Windows users
source .venv/bin/activate # for Linux & Mac users
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Make & apply migrations to your database, in order to create table for menu items:
```bash
cd tree_menu
python manage.py makemigrations
python manage.py migrate
```

Create first superuser:
```bash
python manage.py createsuperuser
```

Launch your project:
```bash
python manage.py runserver
```

## Menu create / edit
Log into your admin panel via endpoint ```127.0.0.1/admin/```, go to "Menu" section and create menu items as follows:
<img src="https://github.com/kopf8/tree_menu/blob/main/1.png" alt="Create necessary menu items in admin" width=500><br>

For each menu item you have to add the following required parameters:
   - Menu name (for instance ```main_menu```)
   - Menu item name (for instance ```About```)
   - **parent** (if applicable)
   - URL - either absolute (for instance ```/about/```), or named (for instance ```about_url```)
   - **order** for sorting on each level

! - Templates for "about", "team", "contacts" and "vacancies" pages were created in this project for demo purposes.

When saved in admin panel, menu structure is being automatically created/updated.

## Using menu in templates

First you need to load the tag into your template:
```
{% load menu_tags %}
```
   
Then you need to draw the menu structure:
```
{% draw_menu 'main_menu' %}
```
where '**main_menu**' is the value of menu_name field, which you have earlier created in admin panel.  

The tag will draw a tree-like menu with the following features:
- All branches are expanded from the root to the active point (based on the URL of the current page)
- First nesting level under the active point is also expanded
- Other branches remain collapsed
- Active menu item is highlighted by the CSS class "active".

<hr>

### Created by:
[✍️ Maria Kirsanova](https://github.com/kopf8) for Uptrade.