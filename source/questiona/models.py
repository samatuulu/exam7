from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=150, null=False, blank=False, verbose_name='Question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.question


class Choice(models.Model):
    answer = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Answer')
    poll = models.ForeignKey('questiona.Poll', related_name='poll_choce', on_delete=models.CASCADE, verbose_name='Poll')

    def __str__(self):
        return self.answer


class Answer(models.Model):
    poll = models.ForeignKey('questiona.Poll', related_name='answer_poll', on_delete=models.CASCADE,
                                 verbose_name='Poll')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    choice = models.ForeignKey('questiona.Choice', related_name='answer_choice', on_delete=models.CASCADE,
                                   verbose_name='Choice')

    def str(self):
        return self.poll