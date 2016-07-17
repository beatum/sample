# Sample Project - Asynchronous tasks in django with django-rq.

This project is scaffolded by Ivan Semernyakov <direct@beatum-group.ru>, read the docs for more details.

Initialize ```virtualenv``` if needed:
```
$ virtualenv {path}
```

Add generated environment variables in ```./.environment``` to ```{virtualenv_path}/bin/activate``` if needed.

(Re)activate ```virtualenv```:
```
$ source {virtualenv_path}/bin/activate
```

Install ```pip``` dependencies using ```./requirements.txt``` they are not already installed:
```
$ pip install -r requirements.txt
```

Apply initial migration:
```
$ python manage.py migrate
```

Create superuser if needed:
```
$ python manage.py createsuperuser
```

Change mode for run.sh:
```
$ sudo su chmod +x run.sh
```

Run:
```
$ ./run.sh
```

### Note Bene

If you want to add new jobs from admin interface, go theare and see at the RQ JOBS. When you will have add new scheduled jobs, each time set arguments as:
```
Args: {"url":"http://sample.com",url":"http://sample.ru"} etc..
```

For monitoring use:
```
http://localhost:8000/admin/rq/ and http://localhost:8000/admin/dashboard/
```

Good luck and best wishes!

That's all!