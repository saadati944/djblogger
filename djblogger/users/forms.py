from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

username_help_text = "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."

password_help_text = """Your password can’t be too similar to your other personal information.<br>
Your password must contain at least 8 characters.<br>
Your password can’t be a commonly used password.<br>
Your password can’t be entirely numeric."""

displayname_help_text = "A name to show in the articles as author's name"

class AuthorUser(ModelForm):
    global username_help_text, password_help_text, displayname_help_text, displayname_help_text
    username = forms.CharField(max_length=150, required = True, help_text = username_help_text)
    # display_name = forms.CharField(max_length=100, required = True, label = "displayname", help_text = displayname_help_text)
    first_name = forms.CharField(max_length=30, required = True)
    last_name = forms.CharField(max_length=150, required = True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, help_text = password_help_text)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']