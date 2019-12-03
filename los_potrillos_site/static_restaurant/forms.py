from django import forms
from static_restaurant.models import Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Name"}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':"Email"}),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':"Phone (Optional)"}),
            'message':forms.Textarea(attrs={'class':'form-control','rows':'4'})
            }
