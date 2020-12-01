from django import forms

# import the models
from myblog.models import Post, Comment

# Form to create post


class PostForm(forms.ModelForm):
    '''
    Model form from model=Post
    '''
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # To get custom styling to forms, adding html field attributes for
        # the<p> classnames refers to the external css library used
        # 'textinputclass' and 'postcontent are custom classes they are need
        # to specify here cz, which are added with django templating in forms.
        widgets = {
            # Bootstrap & medium js fetching classes
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea postcontent'}
            )
        }

# Form to comment a post


class CommentForm(forms.ModelForm):
    '''
    Model form for model=Comment
    '''
    class Meta():
        model = Comment
        fields = ('author', 'text')

        # Similer kind of widgets as PostForm, no 'postcontent' custom class
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea'}
            )
        }
