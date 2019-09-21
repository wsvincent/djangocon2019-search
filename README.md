# Search: From the Ground Up

_Talk given at [DjangoCon US 2019](https://2018.djangocon.us/talk/finally-understand-authentication-in/)_

[Slides available here](https://tinyurl.com/djangocon2019-search)

Search is a fundamental part of most websites but not built into Django itself. This talk explains how search works, how to configure it from scratch in a new project, and looks at built-in full text search options available via PostgreSQL.

---
## Basic Search Set Up
Navigate to the `basic_search` directory and make sure [Pipenv](https://docs.pipenv.org/en/latest/) is installed. Then on the command line:

```
$ pipenv install
$ pipenv shell
(basic_search) $ python manage.py runserver
```

Navigate to [127.0.0.1:8000](127.0.0.1:8000).

When done run `exit` to leave the virtual environment.

## Full Text Search Set Up
Navigate to the `full_text_search` directory and make sure [Docker desktop](https://www.docker.com/products/docker-desktop) is installed and running. Then on the command line:

```
$ docker-compose up -d
```
Navigate to [127.0.0.1:8000](127.0.0.1:8000). When done run `docker-compose down` to stop the running Docker containers.

---
Superuser admin for both is `djangocon` and `testpass123`.
