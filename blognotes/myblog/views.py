# Import FBV classes
from django.shortcuts import render, get_object_or_404, redirect
# Import timezone
from django.utils import timezone
# Importing reverse and reverse_lazy
from django.urls import reverse, reverse_lazy
# Import the CBVs classes
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# Importing the LoginRequiredMixin for CBV and the @login_required decorator
# for fun. based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Import the models and forms
from myblog.models import Post, Comment
from myblog.forms import PostForm, CommentForm

# Create your views here.


class AboutView(TemplateView):
    """
    View for the About page, links the about.html template
    """
    template_name = 'about.html'

# ########################################
# ######## THE CRUD CBVs ############
# ########################################

# CRUD --Retrieval of Information


class PostListView(ListView):
    """
    Views the homepage, list view of posts, post_list.html
    """
    model = Post

    def get_queryset(self):
        """
        Using Django ORM(Object Relational Mapping) with DB, this querysets
        allows perform SQLqueries in a 'pythonish' way,
        which just means from model 'Post' grab all 'objects'(ie posts)
        'filter' it out based on 'published_date'
        attribute less than or equal to(lte) the current time(timezone.now()),
        'order_by' descending order of ("-")
        published date.
        lller SQL query
        'SELECT * FROM Post WHERE published_date <= timezone.now()'
        """
        return Post.objects.filter(published_date__lte=timezone.now()
                                   ).order_by('-published_date')


class PostDetailView(DetailView):
    """
    Detail view of post, post_detail.html
    """
    model = Post

# CRUD --Creating


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    view of formpage to write up the post, similar to 'login_required'
    decorator CBV's got mixins which inherits to the classes provides the same
    functionality that a user must be logged in, to add a post
    """
    # If this view(CreatePostView) is requested, without a login, it must
    # revert to the login page
    login_url = '/login/'
    redirect_field_name = 'myblog/post_detail.html'

    form_class = PostForm
    model = Post

# CRUD --Updating


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    The PostUpdateView is same as CreatePostview, but in here there's only
    updation of the existing one happens
    """
    login_url = '/login/'
    redirect_field_name = 'myblog/post_detail.html'

    form_class = PostForm
    model = Post

# CRUD --Deleting


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    This view Deletes the post from the DB,(DeleteView-manages that)
    if the post is deleted, it takes user back to 'Post list view'
    """
    model = Post
    success_url = reverse_lazy('myblog:post_list')

# ########The CRUD CBV's COMPLETED  ###################
# ######################################################

# Draft View class


class DraftListView(LoginRequiredMixin, ListView):
    """
    Drafts are unpublished blogs, This view is to show them,
    this also need login to see
    """
    login_url = '/login/'
    redirect_field_name = 'myblog/post_list.html'

    model = Post

    def get_queryset(self):
        """
        queryset to find which posts are not published
        by looking up if the 'published_date' == null and order descending by
        created date
        """
        return Post.objects.filter(published_date__isnull=True
                                   ).order_by('-create_date')

# ############ Function Based Views ###################

# To Publish Post


@login_required
def post_publish(request, pk):
    """
    To publish the post, using the method 'publish' in model class 'Post'
    :param request:
    :param pk:
    :return: to the post_detail view of published post
    """
    # Grab the object or return a 404(not found) error
    post = get_object_or_404(Post, pk=pk)
    # call the 'publish' method in 'Post', which adds the current date&time
    # and saves the post to Post model
    post.publish()
    return redirect('myblog:post_detail', pk=post.pk)


# Add comment to post view

@login_required
def add_comment_to_post(request, pk):
    """
    To add a comment when a 'request' with primary key('pk') of post given,
    :param request:
    :param pk:
    :return: the html tag 'form' and the form is created based on logic
    """
    # Grab the object or return a 404(not found) error
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # If the form filled and request submitted
        # get the content to form
        form = CommentForm(request.POST)
        if form.is_valid():
            # checking the form valid or not,
            # if valid save to DB
            comment = form.save(commit=False)
            # post in Comment model foreignkey relation, attach comment to
            # this post
            comment.post = post
            comment.save()
            # after saving redirect to current post_detail page
            return redirect('myblog:post_detail', pk=post.pk)
    else:
        # the form is not posted stay on comment form
        form = CommentForm()
    # render out the html based on 'form' template tagging in
    # 'comment_form.html'
    return render(request, 'myblog/comment_form.html', {'form': form})

# Approve comment view


@login_required()
def comment_approve(request, pk):
    """
    View to approve comment, using the 'approve' method in Comment model,
    ie, when 'approve' method called it sets the boolean value 'True'
    :param request:
    :param pk:
    :return: to the post_detail view of current post
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('myblog:post_detail', pk=comment.post.pk)

# Remove comment view


@login_required()
def comment_remove(request, pk):
    """
    View to Delete a comment, using the 'delete' method in Comment model
    ( native in 'models.Model'), an extra variable required to store the key
    value of comment(ie key of post) to delete
    :param request:
    :param pk:
    :return: to the post_detail view of current post
    """
    comment = get_object_or_404(Comment, pk=pk)
    # variable to store pk
    post_pk = comment.post.pk
    comment.delete()
    return redirect('myblog:post_detail', pk=post_pk)
