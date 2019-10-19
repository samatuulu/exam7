from django.views.generic import ListView

from questiona.models import Choice


class ChoiceListView(ListView):
    template_name = 'choice/choice_index.html'
    context_object_name = 'choice'
    model = Choice

    def get_queryset(self):
        choice = Choice.objects.all()
        return choice