from django.shortcuts import reverse
from django.contrib import messages

class GetSuccessUrlMixin:

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse(self.success_url)
