docker-compose.yml: 34行目を以下のように変える

```
mysite.wsgi
↓
[project_name].wsgi

mysite-nginx
↓
[project_name]-nginx

mysite-db
↓
[project_name]-db

mysite-web
↓
[project_name]-web
```

nginx/conf/nginx.conf.template: 以下のように変える
```
mysite-web
↓
[project_name]-web
```

```sh
$ docker-compose up --build
```

```sh
$ docker-compose run [project_name]-web django-admin startproject [project_name] .
```

settings.pyに以下を追記・修正

```
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
LANGUAGE_CODE = 'ja-JP'
TIME_ZONE = 'Asia/Tokyo'
```

```sh
$ docker-compose run [project_name]-web ./manage.py collectstatic
```

```sh
$ docker-compose up
```

```sh
$ docker-compose run [project_name]-web ./manage.py migrate
```

```sh
$ docker-compose run [project_name]-web ./manage.py createsuperuser
```

アプリケーションの追加
```
$ docker-compose run [project_name]-web ./manage.py startapp [app_name]
```

settings.pyに以下を追記・修正

```
INSTALLED_APPS = [
    ...
    ...
    '[app_name]',
]
```
