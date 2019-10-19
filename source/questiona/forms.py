from django import forms

from questiona.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at']