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
