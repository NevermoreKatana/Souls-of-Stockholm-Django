from django import forms
from souls_of_stockholm.posts.models import Posts, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['name', 'tag', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Название поста'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control',
                                               'multiple': 'multiple',
                                               'required': False}),
        }
        labels = {
            'name': 'Название поста',
            'content': 'Содержание поста',
            'tag': 'Теги',
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['tag'].choices = [(label.id, label.name) for label in Tag.objects.all()]
