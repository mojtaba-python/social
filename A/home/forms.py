from django import forms
from .models import Post_User, Comment


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post_User
        fields = ('body',)

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post_User
        fields = ('body',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widget = {
            'body': forms.Textarea(attrs={'class':'form-control'})
        }

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostSearchForm(forms.Form):
    search = forms.CharField()