#requirements
1. python versi >= 3.9 <= 3.11

#Instalasi
1. git clone https://github.com/badruzbbby/django_tes.git
2. cd django_tes
3. pip install -r requirements.txt
4. edit file settings.py di folder tes_recruitment

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'produk_db',
        'USER': '<username_database>',
        'PASSWORD': '<password database>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. python manage.py makemigrations
6. python manage.py migrate
8. python manage.py fetch_data
7. python manage.py runserver

akses localhost:8000/produk/ untuk melihat data produk

