from django.db.models.fields import AutoField
from django.contrib.auth.forms import UsernameField
from django.forms.fields import IntegerField
from .models import Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
 
        fields = ['comment_user','comment', ]

class createuserform(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        if kwargs: # 내가 추가한 부분
            self.request = kwargs.pop('request') 
        # important to "pop" added kwarg before call to parent's constructor
        super(UserCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(createuserform, self).save(commit=False)
        if commit:
            user.is_active = False
            user.save()

            # Send user activation mail
            current_site = get_current_site(self.request)
            subject = (_('Welcome To %s! Confirm Your Email') % current_site.name)
            message = render_to_string('main/send_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_b64encode(force_bytes(user.pk)),
                'token': PasswordResetTokenGenerator().make_token(user),
            })
            from django.core.mail import send_mail
            send_mail(
                '{}'.format(subject),
                '{}'.format(message),
                'mail.host.kim@gmail.com',
                ['{}'.format(user.email)],
                fail_silently=False,
            )
            # email = EmailMessage(subject, message, to=[user.email])
            # email.send()

        return user
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        field_classes = {'username': UsernameField}
