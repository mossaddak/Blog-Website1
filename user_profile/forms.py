import imp
from xml.dom import ValidationErr
from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


# Sing up
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model
        user = model.objects.filter(username__iexact=username)
        if user.exists():
            raise forms.ValidationError(
                "Ther User already exist with the given username")
        return self.cleaned_data.get('username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model
        user = model.objects.filter(email__iexact=email)
        if user.exists():
            raise forms.ValidationError(
                "The email already exist with the given email")
        return self.cleaned_data.get('email')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password do not match!")
        return self.cleaned_data.get('password')


# update user profile
class UserProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model
        user = model.objects.filter(
            username__iexact=username).exclude(pk=self.instance.pk)
        if user.exists():
            raise forms.ValidationError(
                "Ther User already exist with the given username")
        return self.cleaned_data.get('username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model
        user = model.objects.filter(
            email__iexact=email).exclude(pk=self.instance.pk)
        if user.exists():
            raise forms.ValidationError(
                "The email already exist with the given email")
        return self.cleaned_data.get('email')

    def change_password(self):
        if 'new_password' in self.data and 'confirm_password' in self.data:
            new_password = self.data['new_password']
            confirm_password = self.data['confirm_password']

            if new_password != '' and confirm_password != '':
                if new_password != confirm_password:
                    raise forms.ValidationError("Both passwords not matched!!")
                else:
                    self.instance.set_password(new_password)
                    self.instance.save()

    def clean(self):
        self.change_password()


#profile picture upload
class ProfilePictureUpdateForm(forms.Form):
    profile_image = forms.ImageField(required=True)