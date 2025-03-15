from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
     )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        )

    class Meta:
        model = User
        fields = ['username','email','first_name']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            # 'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'opass'})
            }