from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    title = forms.CharField(label="title",max_length=30,widget=forms.TextInput(attrs={"class":"form-title","placeholder":"Enter the title"}))
    body = forms.CharField(label="description",widget=forms.Textarea(attrs={"class":"form-body","rows":10,"placeholder":"Enter the description"}))
    class Meta:
        model = Todo
        fields = ['title','body']
    # Add a validation check
    # self referes to form instance and access the form fields and perform validation within the method
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise forms.ValidationError("Title must be more than 2 characters")
        return title
    def clean_body(self):
        body = self.cleaned_data['body']
        if len(body) > 100:
            raise forms.ValidationError("Description exceeds max limit")
        return body


    title = forms.CharField(label="title",max_length=30,widget=forms.TextInput(attrs={"class":"form-title","placeholder":"Enter the title"}))
    body = forms.CharField(label="description",widget=forms.Textarea(attrs={"class":"form-body","rows":10,"placeholder":"Enter the description"}))
    