# CSS Background

## Description

`css_background` is a [django-cms](https://github.com/divio/django-cms) plugin which allow you to edit css background image or color from the edit mode

## Depends

- [django-cms](https://github.com/divio/django-cms)
- [cms_placeholder_attr](https://github.com/WnP/cms_placeholder_attr)
- [django-filer](https://github.com/stefanfoulis/django-filer)

## Usage

you can define your template like this:

```django
{% load placeholder_tags placeholder_attr %}

<div style="{% placeholder_attr 'My Background Css Placeholder' 'CssBackground' 'css_background' %}">
  {% placeholder 'My Background Css Placeholder' %}
</div>
```

after that set the provide a `CSS Background` plugin for this placeholder, and chose an image, or set rgb or rgba for a colored background
