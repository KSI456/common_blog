from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
 
        fields = ['comment_user','comment', ]