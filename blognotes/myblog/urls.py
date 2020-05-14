from django.urls import path

# Importing views
from myblog import views

app_name = 'myblog'

urlpatterns = [
    ### Class Based Views
    # homepage, about Page, Create Post views
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    ## Views that require primary key input
    # Detail view, Update View and Delete view
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    # Draft List View
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),

    ### Function Based Views
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]