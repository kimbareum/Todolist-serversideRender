from django import forms
from .models import User


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '15'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '20'}))


class SignUpForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '15', 'placeholder': '15자 이내로 입력해주세요.'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'minlength': '8', 'maxlength':'20', 'placeholder': '8-20자 이내로 입력해주세요.'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'minlength': '8', 'maxlength':'20', 'placeholder': '비밀번호를 다시 한번 입력해주세요.'}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '15', 'placeholder': '15자 이내로 입력해주세요.'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('이미 사용 중인 사용자명입니다.')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

        return cleaned_data

