from django import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(UserLoginForm, self).clean(*args, **kwargs)

from .models import Word

def word(request):
    level = request.GET.get('level')
    if level:
        words = Word.objects.filter(level=level)
        return render(request, 'word.html', {'words': words})
    else:
        return redirect('learn')