# How to do things

---

## Adding a custom filter in django

---

To add a custom filter to django app/project, place the scripts in the recommended path\
Refer the official [documentation](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/).

> Path: <app_name>/templatetags(package with \_\_init\_\_.py)/my_filter.py

To use a filter it needs to [register](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#registering-custom-filters) them, then load it and use in jinja templates.

1. Adding a print debugging script as a custom filter(Not exactly a filter, cz it did not got anything to do with the templates, but only with the .py files print debugging)

### The print debugging script

```python
from inspect import currentframe

def dPrint(content=''):
    """Generate a debug print line
    as a modifier to the original print function

    Args:
        content (): the content to be printed to the terminal
    """
    print(f"{currentframe().f_back.f_lineno}: {content}")


dPrint()
# 26:
# Where 26 is the line number where the print called

```

## Adding committed files back to .gitignore

---

Getting that earlie commited files away from repository also without deleting from local, here in the old version of the project, I've pushed the pycache files too, but now I need to add them in git ignore, simply adding a `\*.pyc`, didn't got any effect cz, it is already in the repository tracked,
need to remove them with

```bash
# Remove the files from the repo, but keep the local cache

git rm --cached <path to the file>
# for a folder
git rm -r --cached <folder>

# here for the __pycache__
git rm  blognotes/myblog/__pycache__/

```

It will remove the the files from repo and stage the deletions for the commit.

## View the sqlite tables visually online

---

To view the model tables and foreign key relations visually one can use the free online tool,
[sqliteonline.com](https://sqliteonline.com/).

click file open db -> add the **db.sqlite3** file created after the django migration and click on view table.

## The "related name" argument in the Django ORM foreign key relation

---

In the project the comments are related to the post through a foreign key, (simply the comment model stores the post_id)..\
with,

```python
class Comment(models.Model):
   post = models.ForeignKey(
           'myblog.Post', related_name='comments', on_delete=models.CASCADE)
```

Then there is this method in the Post model,

```python
def approve_comments(self):
   return self.comments.filter(approved_comment=True)
```

Look at this answer from [stackoverflow](https://stackoverflow.com/a/2642645/12167598)

As the foreign key creates a reverse relation between 'myblog.Post' model to the Comment.post field, if one not specify a related name django will automatically create a new one with "comment_set",

Then it can be accessed from parent model ie, Post.comment_set.all()

By setting a related_name(plural, foreignkey returns multiple objects), here related_name='comments',
so, Post.comments can be used for all the comments related to the post.

## `save` method in model.

* [The `save`](https://docs.djangoproject.com/en/3.1/topics/db/queries/#creating-objects) performs an INSERT SQL statement behind the scenes
* The create() method can be used to create and save at the same time
* Look for more info on [save method](https://docs.djangoproject.com/en/3.1/ref/models/instances/#saving-objects) on Django.

### `get_absolute_url` method of Django models

* The Django [`get_absolute_url`](https://docs.djangoproject.com/en/3.1/ref/models/instances/#get-absolute-url) tells how to calculate the canonical URL for an object. To callers, this method should appear to return a string that can be used to refer to the object over HTTP.

## Setting the Login and Logout redirect URL's

* The login and logout redirect urls can be defined on the settings.py, So the Django Auth(django.contrib.auth.views) will redirect to that pages after a login and logout.

  ```python
  # Login, logout redirect to home
  LOGIN_REDIRECT_URL = '/'
  LOGOUT_REDIRECT_URL = '/'
  ```

## Hosting the site in [pythonanywhere.com](https://www.pythonanywhere.com/)

* Create a beginner account (512mb disc, console)
* Set up a virtual environment for the project

  ```bash
    > mkvirtualenv --python=python3.8 myproject
    # myproject is the env name
  ```

* It creates a new python executable in `/home/Akshay203/.virtualenvs/myproject/bin/python3.8`.
* Use the `pip list` to list installed packages.
* Clone the project to the remote server from github, `git clone <path>`
* Now the working path is `/home/Akshay203/<pr_name>/<git_mainfolder>/project`
* Install the requirements in the venv, `pip install -r requirements.txt`
* Check install using `which django-admin.py`, that shows the django-admin path.
* Make migrations and set the superuser.(testuser & testproject#1)

### Setting Up the Dashboard

* Go to **web** --> Add new web apps
* You can only set the given domain name as it is the basic version (Akshay203.pythonanywhere.com.), click next
* Next option is to select the web framework, select the "manual configuration", then select the python version (here 3.8) and virtualenv, the setup will create a sample hello world WSGI(Web Server Gateway Interface) file, which the interface file for python web apps django comes with its full support.
*  Now the app is set up, need to change the settings and paths for its running.
* Go down and enter the path to `virtualenv` first, `/home/Akshay203/.virtualenvs/myproject`
* Setting the `code` path: Get the code path by running `pwd` (here: `/home/Akshay203/Blognotes-Django-simple-blog-project/blognotes`)
* WSGI file Edit\
  Edit the WSGI file,
  * Delete the hellow world files(usually from line no 13 to 47), then

    ```python
      import sys
      import os

      # assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
      path = '/home/Akshay203/Blognotes-Django-simple-blog-project/blognotes'

      os.chdir(path)
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blognotes.settings")


      # +++++++++++ DJANGO +++++++++++
      # To use your own django app use code like this:

      ## then:
      import django
      django.setup()

      from django.core.wsgi import get_wsgi_application
      application = get_wsgi_application()
    ```

* Admin - corrections for static files
  url:-  /static/admin
  directory_path:- /home/Akshay203/.virtualenvs/myproject/lib/python3.8/site-packages/django/contrib/admin/static/admin

* User Static files
  url:-  /static/
  directory_path:- /home/Akshay203/Blognotes-Django-simple-blog-project/blognotes/myblog/static

* Add the host url to the ALLOWED_HOSTS in settings.py,\
  ALLOWED_HOSTS = ['Akshay203.pythonanywhere.com']

* Change debug mode to 'False', not to display debug messages.
* Now the site will be hosted.
