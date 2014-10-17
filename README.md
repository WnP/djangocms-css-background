# CSS Background

## Description

`djangocms-css-background` is a [django-cms](https://github.com/divio/django-cms) plugin which allow you to edit css background image or color from the edit mode

## Depends

- [django-cms](https://github.com/divio/django-cms)
- [djangocms-placeholder-attr](https://github.com/WnP/cms_placeholder_attr)
- [django-filer](https://github.com/stefanfoulis/django-filer)


## Installation

* use pip `pip install djangocms-css-background`
* Syncronize the models: `python manage.py syncdb` (with south or django 1.7 use migrations)
* Put in your INSTALLED_APPS: `INSTALLED_APPS += ('djangocms-css-background', )`


## Usage

you can define your template like this:

```django
{% load placeholder_attr %}

<div style="{% placeholder_attr 'My Background Css Placeholder' 'CssBackground' 'css_background' %}">
  {% placeholder 'My Background Css Placeholder' %}
</div>
```

remember to set the same name of a placeholder in the placeholder_attr name parameter.

after that set the provide a `CSS Background` plugin for this placeholder, and chose an image, or set rgb or rgba for a colored background
