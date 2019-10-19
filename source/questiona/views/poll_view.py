from django.urls import reverse
from django.views.generic import ListView, DetailView

from questiona.models import Poll


class PollListView(ListView):
    template_name = 'poll/poll_index.html'
    context_object_name = 'poll'
    model = Poll

    def get_queryset(self):
        poll = Poll.objects.order_by('-created_at')
        return poll


class PollDetailView(DetailView):
    template_name = 'poll/poll_detail.html'
    context_object_name = 'poll'
    model = Poll

    def get_success_url(self):
        return reverse('poll_detail.html')