from django.shortcuts import render
from .models import Profile
from .models import DogRun
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView

# Create your views here.


class ProfileUpdateView(UpdateView):
    model =  Profile
    fields = ['name','breed','birthday','personality','allergy','memo','profile_image','rabies_vaccine_date',
              'mixed_vaccine_date','mixed_vaccine_type',]
    template_name = 'dogruns/profile_form.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'dogruns/profile_detail.html'
    
    
    success_url = reverse_lazy('dogruns:profile_form')
    
    
class MyPageView(DetailView):
    model = Profile
    template_name = 'dogruns/mypage.html'
    context_object_name = 'profile'
    
class DogRunListView(TemplateView):
    template_name = 'dogruns/index.html'
    
class DogRunListView(ListView):
    model = DogRun
    template_name = 'dogruns/dog_list.html'
    context_object_name = 'dogruns'
    
class DogRunCreateView(CreateView):
    model = DogRun
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['appeal'].widget.attrs['placeholder'] = (
            '例：天然芝で広々したドッグランです')
        form.fields['memo'].widget.attrs['placeholder'] = (
            '例：土日は混雑します')
        return form
    