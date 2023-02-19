from django import forms

from .models import Video


class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'thumbnail', 'upload']
        """ フォームの内容を以下のように記述することも可能 """
        widgets = {
            # <input name="title" type="text" class="form-control"
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            # <textarea name="description" class="form-control"
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            # <input name="thumbnail" type="file" class="form-control-file"
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
            # <input name="upload" type="text" class="form-control"
            'upload': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            })
        }
