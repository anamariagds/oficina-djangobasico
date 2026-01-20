### branch "init-projeto-01"
> django-admin startproject blog .

### Demonstrações:
> python manage.py runserver 

- LANGUAGE_CODE = 'pt-br'

- TIME_ZONE = 'America/Sao_Paulo'

### branch "cria-app-02"
> python manage.py startapp post

### branch "primeira-view-03"
- View que retorna texto simples
- url 'home'

### branch "view-lista-post-04"
- Apresentar admin
- criar model de post
- Registrar model no admin
> python manage.py magemigrations
> python manage.py migrate
#### Criar super usuário
> python manage.py createsuperuser
- popular bd
- View que lista posts criados