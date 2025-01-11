#Instalasi
1. git clone https://github.com/badruzbbby/django_tes.git
2. cd django_tes
3. pip install -r requirements.txt
4. edit file settings.py 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'produk_db',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver

akses localhost:8000/produk/ untuk melihat data produk

