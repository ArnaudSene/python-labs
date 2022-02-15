#  Django 4.0 Swagger OpenAPI 3.0 Postgres 2.5 Python 3.9
- PYTHON 3.9 
- DJANGO 4.0
- POSTGRES 2.5
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
```

### Swagger-ui OpenAPI 3.0
- http://127.0.0.1:8000/schema/
- http://127.0.0.1:8000/swagger/

### REST API
- http://127.0.0.1:8000/api/
- http://127.0.0.1:8000/api/users
- http://127.0.0.1:8000/api/groups

### REST API Auth
- http://127.0.0.1:8000/auth/password/reset/
- http://127.0.0.1:8000/auth/password/reset/confirm/
- http://127.0.0.1:8000/auth/login
- http://127.0.0.1:8000/auth/logout
- http://127.0.0.1:8000/auth/user
- http://127.0.0.1:8000/auth/password/change/

### Django Admin
- http://127.0.0.1:8000/admin/

