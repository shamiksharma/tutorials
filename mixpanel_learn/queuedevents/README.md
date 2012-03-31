Using mixpanel-celery to send messages.
Kestrel is the other option (but uses a JMS message queue, so heavy-weight)

- Verify django installed

% source ~/proj/venv/bin/activate
(venv)% python 
>> import django      # works

- Create a django project

> (venv)%  python startproject  mysite
> (venv)%  cd mysite
> (venv)%  python manage.py runserver

- Create a view.

> (venv)%  cd mysite/mysite   # same level as manage.py
> (venv)%  edit views.py      # create simple view
> (venv)%  edit urls.py       # point to the view
> (venv)%  python manage.py runserver

- 


