# Django-learning-blog-project

---

<img src="./blog_notes.png" width="250" height="auto">

[CHECK OUT THE SITE HERE](http://akshay203.pythonanywhere.com/)\
(use username:testuser, psw: testproject#1)

This is a basic multi user blog site made with django (ver 3.0.11), and bootstrap.

* Login, Logout application.
* Create posts add comments on them, do an edit or delete them
* Posts and comments need to be approved by an authenticated user for publishing
* Unapproved posts put in the drafts section.
* Uses a [medium-style text editor](https://github.com/yabwe/medium-editor)

## How to run it locally

* Clone the project to local
* Create your own python virtual environment (uses python ver 3.8), with `python -m venv <environment_name>`
* `cd` to the base path, with pip installed use. `pip install -r requirements.txt` to install all the dependencies and django.
* Run the migrations to apply the db contents,

  ```python
    python manage.py migrate
    python manage.py makemigrations myblog
    python manage.py migrate
  ```

* Then run the local server with `pyton manage.py runserver`, that will outs the app at local and port: 8000, (127.0.0.1:8000), go to the address in the browser to view it locally.