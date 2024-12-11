from django import forms

from moniTouring.common.models import Review


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search Monitor:',
            }
        )
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_text',)
        widgets = {
            'review_text': forms.Textarea(attrs={'placeholder': 'Add review:', })
        }


class ReviewEditForm(ReviewForm):
    class Meta:
        model = Review
        fields = ('review_text',)
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Edit Review:',
            }
        )


class ReviewDeleteForm(ReviewForm):
    class Meta:
        model = Review
        fields = ('review_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance