from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .models import Book, UserProfile



from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')


# User = get_user_model()
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'description', 'published_date']

#     def clean_title(self):
#         title = self.cleaned_data.get('title')
#         if "<script>" in title.lower():
#             raise forms.ValidationError("Title contains invalid characters.")
#         return title

#     def clean_description(self):
#         description = self.cleaned_data.get('description')
#         if "<script>" in description.lower():
#             raise forms.ValidationError("Description contains invalid characters.")
#         return description
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
#     date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
#     profile_photo = forms.ImageField(required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'confirm_password', 'date_of_birth', 'profile_photo']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm = cleaned_data.get("confirm_password")

#         if password and confirm and password != confirm:
#             raise forms.ValidationError("Passwords do not match.")

#         return cleaned_data


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
