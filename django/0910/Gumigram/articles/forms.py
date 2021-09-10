from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='TITLE :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3 text-white bg-secondary',
                'placeholder': 'Enter the title',
                'style': 'font-family: paralucent, sans-serif;',
            }
        )
    )

    content = forms.CharField(
        label='CONTENT :',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control mb-3 text-white bg-secondary',
                'placeholder': 'Enter the content',
                'style': 'font-family: paralucent, sans-serif;',
            }
        )
    )

    image = forms.ImageField(
        label='IMAGE ',
        allow_empty_file=True,
        widget=forms.FileInput(
            attrs={
                'type': 'file',
                'accept': 'image/*',
                'style': 'font-family: paralucent, sans-serif;',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
