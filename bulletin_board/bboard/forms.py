from django.forms import ModelForm

from .models import Bb


class BbForm(ModelForm):
    """ The shape class associated with the Bb model.
    The form is used to enter new ads"""

    class Meta:
        """Here are the form options."""
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')