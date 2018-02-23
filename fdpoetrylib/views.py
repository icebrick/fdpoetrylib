# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm


class IndexView(TemplateView):
    '''首页视图'''
    template_name = 'index.html'


class AccountProfileView(LoginRequiredMixin, TemplateView):
    '''用户个人中心视图'''
    template_name = 'account_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

def register_view(request):
    '''注册视图'''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
