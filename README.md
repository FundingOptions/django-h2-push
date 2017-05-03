# django-h2-push

Adds http2 preload headers to be send to the server

Usage
=====

In the template, add new prefetches with
```html
<html>
<body>
<img src="{% pushed_static 'my_image.png' %}"/>
</body>
</html>
```

it will render to

```html
<html>
<body>
<img src="my_image.png"/>
</body>
</html>
```

and add the link headers in the middleware:

```
Link: "<my_image.png>; rel=preload"
```

