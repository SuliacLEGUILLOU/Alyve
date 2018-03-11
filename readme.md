## Alyve

Source code of [alyve](https://www.alyve.be)
It stills in development, I listening any advice or sugggestions.

## Install

Alyve is really simple to install, everything you need is included in file `requirements.txt` and virtualenv installed.

```
$ virtualenv -p python3 alyve-env
$ source alyve-env/bin/activate
$ git clone git@github.com:Aly-ve/Alyve.git
$ cd Alyve/
$ pip3 install -r requirements.txt
$ python3 manage.py makemigrations blog
$ python3 manage.py migrate
$ python3 managy.py createsuperuser
```

Create your blog on table `blog` (only one record!) and enjoy it.


# Deploy

Alyve runs with Gunicorn and a systemd deamon.
Copy the file `alyve.service` in `/etc/systemd/system/alyve.service`.
Now, you need to enable the service at start: 

```
# systemd enable alyve.service
# systemd start alyve.service
```

### Don't forget to change paths on `alyve.service` and `gunicorn_start.sh` !

## Nginx
With Nginx, you need to add these lines in your `sites-available` and create the link between `sites-available` and `sites-enabled`.

```nginx
location /uploads {
        alias /home/alysson/Development/alyve/uploads;
}

location /static {
        alias /home/alysson/Development/alyve/static2;
}

location / {
        include proxy_params;
        proxy_pass http://unix:/home/alysson/Development/alyve/gunicorn.sock;
}
```

## Migrate

To migrate database and apply modifications, you need to follow these lines when Alyve isn't running:

```
$ python3 manage.py makemigrations blog
$ python3 manage.py migrate
$ python3 managy.py collectstatic
```

And restart Alyve.