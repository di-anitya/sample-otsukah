from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'testings/index.html'

  def get_queryset(self):
    pass