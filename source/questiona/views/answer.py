from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from questiona.models import Poll, Choice, Answer


class Quiz(View):
    def get(self, request, *args, **kwargs):
        poll = self.get_poll()
        return render(request, 'answer/answer.html', {'poll': poll})

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def post(self, request, *args, **kwargs):
        poll_id = kwargs.get('pk')
        choice_id = int(request.POST.get('answer'))
        ans_pol = get_object_or_404(Poll, pk=poll_id)
        choice = get_object_or_404(Choice, pk=choice_id)
        answer = Answer()
        answer.poll = ans_pol
        answer.choice = choice
        answer.save()
        return redirect('index')