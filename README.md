# PYTHON DJANGO v1
- POSTGRES

## URLS definition
```python
admin/
[name='home']
create/ [name='create-post']
update/<str:slug>/ [name='update-post']
delete/<str:slug>/ [name='delete-post']
<str:slug>/ [name='show-post']
```

### Django Admin
- http://127.0.0.1:8000/admin/

### Apps Blog
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/create/
- http://127.0.0.1:8000/someting-new/?
- http://127.0.0.1:8000/update/someting-new/
- http://127.0.0.1:8000/delete/someting-new/
