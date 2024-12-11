from django import forms

from moniTouring.monitors.models import Monitor


# Create your forms here.


class BaseForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['name', 'photo', 'price', 'brand', 'size', 'refresh_rate', 'brightness', 'resolution', 'extra_characteristics',]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Monitor name',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
            'brand': forms.Textarea(
                attrs={
                    'placeholder': 'Brand',
                }
            ),
            'size': forms.NumberInput(
                attrs={
                    'placeholder': 'Inches',
                }
            ),
            'refresh_rate': forms.NumberInput(
                attrs={
                    'placeholder': 'Hertz',
                }
            ),
            'brightness': forms.NumberInput(
                attrs={
                    'placeholder': 'Brightness',
                }
            ),
            'resolution': forms.Textarea(
                attrs={
                    'placeholder': 'Resolution',
                }
            ),
            'extra_characteristics': forms.Textarea(
                attrs={
                    'placeholder': 'Extra details',
                }
            ),
        }
        labels = {
            'extra_characteristics': 'Extra',
        }


class MonitorAddForm(BaseForm):
    pass


class MonitorEditForm(BaseForm):
    class Meta:
        model = Monitor
        fields = ['name', 'photo', 'price', 'brand', 'size', 'refresh_rate', 'brightness', 'resolution', 'extra_characteristics',]


class MonitorDeleteForm(BaseForm):
    class Meta:
        model = Monitor
        fields = ['name', 'photo', 'price', 'brand', 'size', 'refresh_rate', 'brightness', 'resolution', 'extra_characteristics',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance