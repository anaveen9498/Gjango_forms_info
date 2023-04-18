from django import forms
A=[('MALE','male'),('FEMALE','female'),('TRANGENDER','BOTH')]
C=[('JAVA','java'),('PYTHON','python'),('MEARN','mearn')]
class studentinfo(forms.Form):
    Name=forms.CharField(max_length=40)
    Age=forms.IntegerField()
    Email=forms.EmailField()
    Date=forms.DateField()
    url=forms.URLField()
    timedate=forms.DateTimeField()
    Gender=forms.ChoiceField(choices=A)
    Skills=forms.MultipleChoiceField(choices=C)
    Course=forms.MultipleChoiceField(choices= C,widget=forms.CheckboxSelectMultiple)
    Radio=forms.ChoiceField(choices=A,widget=forms.RadioSelect)