from django import forms
from django.contrib.auth.models import User



class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter User Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Confirm Password'}))
    class Meta():
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']
        #widgets = {'password':forms.PasswordInput}

    def clean(self):
        cleaned_data = super(SignUpForm,self).clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        inputpassword = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if len(inputpassword)<8:
            raise forms.ValidationError('Password should contains minimum 6 characters')

        if inputpassword != confirm_password:
            raise forms.ValidationError('Password not matched')

































#def clean_email(self):
    #cleaned_data = super(SignUpForm, self).clean()
    #email = cleaned_data.get('email')
    #username = cleaned_data.get('username')

    #if email and User.objects.filter(email=email).exclude(username=username).count():
    #    raise forms.ValidationError(
    #        ("This email address is already in use. Please enter a different email address."))
    #return email