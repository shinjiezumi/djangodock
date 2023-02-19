from django import forms

from .models import Comment


class CommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 全てのフィールドに form-control クラスを付与する. bootstrap向け
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ['name', 'text']
