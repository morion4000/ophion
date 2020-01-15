from django import forms
from lists.models import List


class ListForm(forms.ModelForm):

    class Meta:
        model = List

        fields = ('name', 'description')
