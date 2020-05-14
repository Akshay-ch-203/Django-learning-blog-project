from django.db import models

#To add current time to posts based on UTC in settings.py
from django.utils import timezone

from django.urls import reverse

# Create your models here.
# Model to store each blog post,

class Post(models.Model):
    '''
    model class to store the Post
    fields: author, title, text, creation date, publication date
    '''
    # Only authorized(superuser) users can add a new post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    
    def publish(self):
        '''
        method in model 'Post', a post is only added to the model
        after publish, with published 'date & time'
        '''
        self.published_date = timezone.now()
        self.save()
        
    def approve_comments(self):
        '''
        Any one can comment on a post, but all of them not gonna get approved,
        This method filters out unapproved(approved_comment = False) comments from Comment class,
        So that only approved(approved_comment = True) comments save to the model 'Post'
        '''
        # This 'Post' model and the following 'Comment' model related with a ForeignKey,
        # Each comment is attached to a 'Post', the name 'comments' is the 'related_name' in the relation
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        '''
        After Someone creates a post, the user need to be taken to the posts
        detailed view page('post_detail'),
        Detailed view always needs the primary key(pk) to display/identify the post
        'self.pk' represents return to the detailed view of same post after creating
        '''
        return reverse("myblog:post_detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    
# Model to store comments

class Comment(models.Model):
    '''
    The Comment model class is attached to Post--ForeignKey,
    Anyone can put a comment to a post but it need to get approved, an approved_comment attribute
    so added extra to this Comment class
    '''
    # 'myblog.Post' refers to myblog-->models.py-->Post model,
    post = models.ForeignKey('myblog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        '''
        To approve a comment and save to db
        '''
        self.approved_comment = True
        self.save()
        
    def get_absolute_url(self):
        '''
        return to the list view(ie the homepage) after commenting on
        a post, the comments needs approval to display
        '''
        return reverse("post_list")
        
    def __str__(self):
        return self.text