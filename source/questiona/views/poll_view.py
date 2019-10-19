from django.views.generic import ListView

from questiona.models import Poll


class PollListView(ListView):
    template_name = 'poll/poll_index.html'
    context_object_name = 'poll'
    model = Poll

    def get_queryset(self):
        poll = Poll.objects.order_by('-created_at')
        return poll