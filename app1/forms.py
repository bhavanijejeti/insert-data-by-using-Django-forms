from django import forms
t=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('django','DJANGO')]
class signupforms(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    email=forms.EmailField()
    Password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=t,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)

