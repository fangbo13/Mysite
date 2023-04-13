from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Person
from .forms import ContactForm
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = 'intro/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        return context
    
class ContactView(TemplateView):
    template_name = 'intro/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # 处理表单数据
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # 发送电子邮件等其他操作
            # 最后重定向到成功页面或返回一个成功消息
            return HttpResponseRedirect('/success/')
        else:
            # 处理无效表单数据或提供适当的错误消息
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
