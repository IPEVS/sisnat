# Sisnat-IPEVS
 Sisnat-IPEVS

## Run with docker on dev mode

    $ make build
    $ make up

If you are using postgres you need check and run before `make up`:

    1. Uncomment postgres/.env
    2. run: $ make create-db

```shell
$ sudo rm -rf local/ #Apagar a pasta local onde esta o db
$ docker-compose build --no-cache
$ docker-compose ps
$ make build
$ make create-db #Criar novo db
$ make up
$ make cmd #Acessar o container #Para fazer isso no Shell basta usar "python manage.py shell"
$ ./manage.py makemigrations
$ ./manage.py migrate
```
## [Deploy HEROKU](https://testdriven.io/blog/deploying-django-to-heroku-with-docker/#project-setup)

```shell
$ heroku container:login
$ ./deploy.sh
```