from django import forms
from django.forms import widgets
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widgets=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title'
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(attrs = {
        #         'class': 'title',
        #         'placeholder': 'Enter the title',
        #         'maxlength': 10,
        #     })
        # }


# class ArticleForm(forms.Form):
#     REGION_1 = 'sl'
#     REGION_2 = 'dj'
#     REGION_3 = 'gm'
#     REGION_4 = 'gj'
#     REGION_5 = 'bs'
#     REGION_CHOICE = [
#         (REGION_1, 'Seoul'),
#         (REGION_5, 'Daejeon'),
#         (REGION_2, 'Gumi'),
#         (REGION_3, 'Gwangju'),
#         (REGION_4, 'Busan'),
#     ]
#     region = forms.ChoiceField(choices=REGION_CHOICE, widget=forms.Select)