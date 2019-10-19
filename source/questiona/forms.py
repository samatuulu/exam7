from django import forms

from questiona.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['answer']


class AnswerFrom(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['poll']