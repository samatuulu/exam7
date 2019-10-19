from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from questiona.forms import ChoiceForm
from questiona.models import Choice


class ChoiceListView(ListView):
    template_name = 'choice/choice_index.html'
    context_object_name = 'choice'
    model = Choice

    def get_queryset(self):
        choice = Choice.objects.all()
        return choice


class ChoiceCreateView(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse('poll')


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm
    context_key = 'choice'

    def get_success_url(self):
        return reverse('choice')


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/choice_delete.html'
    context_object_name = 'choice'
    success_url = reverse_lazy('choice')