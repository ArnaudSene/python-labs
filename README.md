# PYTHON DJANGO v3
- POSTGRES
- REST API
- SWAGGER API 

> SWAGGER API user drf-yasg (https://drf-yasg.readthedocs.io/en/stable/index.html, https://github.com/axnsan12/drf-yasg)
> 
{.is-info}

## URLS definition
```python
^swagger(?P<format>\.json|\.yaml)$ [name='schema-json']
^swagger/$ [name='schema-swagger-ui']
^redoc/$ [name='schema-redoc']
api/
admin/
dj-rest-auth/ password/reset/ [name='rest_password_reset']
dj-rest-auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
dj-rest-auth/ login/ [name='rest_login']
dj-rest-auth/ logout/ [name='rest_logout']
dj-rest-auth/ user/ [name='rest_user_details']
dj-rest-auth/ password/change/ [name='rest_password_change']
[name='home']
create/ [name='create-post']
update/<str:slug>/ [name='update-post']
delete/<str:slug>/ [name='delete-post']
<str:slug>/ [name='show-post']
```


## URLs Example
### Swagger API
- http://127.0.0.1:8000/swagger
- http://127.0.0.1:8000/redoc

### REST API
- http://127.0.0.1:8000/api/
- http://127.0.0.1:8000/api/me
- http://127.0.0.1:8000/api/posts-list/

### RESP API User management
- http://127.0.0.1:8000/dj-rest-auth/login/
- http://127.0.0.1:8000/dj-rest-auth/login/
- http://127.0.0.1:8000/dj-rest-auth/logout

### Django Admin
- http://127.0.0.1:8000/admin/

### Apps Blog
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/create/
- http://127.0.0.1:8000/someting-new/?
- http://127.0.0.1:8000/update/someting-new/
- http://127.0.0.1:8000/delete/someting-new/
