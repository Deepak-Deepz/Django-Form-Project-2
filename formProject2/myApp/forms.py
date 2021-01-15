from django import forms
class Feedback(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    email = forms.EmailField()
    comments = forms.CharField(widget = forms.Textarea)
    def clean_name(self):
        n = self.cleaned_data['name']
        if(len(n)>10):
            raise forms.ValidationError("Number of Characters Must be less than 10")
        return n
    def clea_roll(self):
        r1 = self.cleaned_data['roll']
        r =str(r1)
        if(len(n)>=4):
            raise forms.ValidationError("roll number should be less 4 digits")
        return r
