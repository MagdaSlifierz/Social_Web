from django import forms
from .models import Images

class ImagesCreateForm(forms.ModelForm):
    class Meta:
        mode = Images
        fields = ['title','url','description']
        widgets = {
            'url' : forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not ' \
                                        'match valid image extensions.')