# PYTHON DJANGO v2
- POSTGRES
- REST API
- SWAGGER OpenAPI 3.0

## URLS definition
```python
schema/ [name='schema']
swagger/ [name='swagger-ui']
api/
admin/
auth/ password/reset/ [name='rest_password_reset']
auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
auth/ login/ [name='rest_login']
auth/ logout/ [name='rest_logout']
auth/ user/ [name='rest_user_details']
auth/ password/change/ [name='rest_password_change']
[name='home']
create/ [name='create-post']
update/<str:slug>/ [name='update-post']
delete/<str:slug>/ [name='delete-post']
<str:slug>/ [name='show-post']
```

### Swagger-ui OpenAPI 3.0
- http://127.0.0.1:8000/schema/
- http://127.0.0.1:8000/swagger/

### REST API
- http://127.0.0.1:8000/api/
- http://127.0.0.1:8000/api/users
- http://127.0.0.1:8000/api/groups
- http://127.0.0.1:8000/api/posts-list/

### REST API Auth
- http://127.0.0.1:8000/auth/password/reset/
- http://127.0.0.1:8000/auth/password/reset/confirm/
- http://127.0.0.1:8000/auth/login
- http://127.0.0.1:8000/auth/logout
- http://127.0.0.1:8000/auth/user
- http://127.0.0.1:8000/auth/password/change/

### Django Admin
- http://127.0.0.1:8000/admin/

### Apps Blog
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/create/
- http://127.0.0.1:8000/someting-new/?
- http://127.0.0.1:8000/update/someting-new/
- http://127.0.0.1:8000/delete/someting-new/
