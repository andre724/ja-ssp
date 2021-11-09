from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from accounts.models import SSPUser
import re




class RegisterForm(UserCreationForm):
    '''
    Personalized form that inherits from UserCreationFomr
    '''

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = SSPUser
        fields = ["email","username","password1","password2"]

    def clean_email(self):
        '''
        Cleans the data from EmailField and validates 
        '''
        email = self.cleaned_data.get('email')
        if '@nokia.com' in email:
            return email
        else:
            raise forms.ValidationError('Inserted e-mail is not from a Nokia account')

    def clean_password1(self):
        '''
        Since UserCreationForm already cleans the passwords this function only adds
        another validator that checks if the password1 has an Upper case letter,special char and 1 digit.
        '''
        password1 = str(self.cleaned_data.get('password1'))
        upper_check= re.search(r'[A-Z]',password1)
        digit_check = re.search(r'\d',password1)
        specialchar_check = re.search(r'\W',password1)
        
        if upper_check and digit_check and specialchar_check:
            
            return password1
        else:
            
            raise forms.ValidationError('The password1 must contain at least 1 upper case letter, 1 special character and 1 digit.')


class LoginUserForm(forms.Form):
    '''
    Form for the Log in page
    '''
    email = forms.EmailField(
        label= ("email")
    )
    password = forms.CharField(
        label=("password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password1'}),
    )
    class Meta:
        model = SSPUser
        fields= ['email','password']