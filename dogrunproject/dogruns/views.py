from django.shortcuts import render,get_object_or_404
from .models import Profile
from .models import DogRun
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,View
from dogruns import views
import dogruns
# Create your views here.

#プロフィール登録
class ProfileUpdateView(UpdateView):
    model =  Profile
    fields = ['name','breed','birthday','personality','allergy','memo','profile_image','rabies_vaccine_date',
              'mixed_vaccine_date',]
    template_name = 'dogruns/profile_form.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'dogruns/profile_detail.html'
    
    
    success_url = reverse_lazy('dogruns:profile_form')
    
from django.views.generic import ListView

#マイページ
class MyPage(DetailView):
    model = Profile
    template_name = "dogruns/mypage.html"   
    context_object_name = "profile" 
    
#ドッグラン施設登録ページ
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
    
    from django.views.generic import ListView

class DogRunListView(ListView):
    model = DogRun
    template_name = 'dogruns/dog_list.html'
    context_object_name = 'dogruns'

#マイページにプロフィールを反映させる
class MyPage(TemplateView):
    template_name = "dogruns/mypage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["profile"] = Profile.objects.last()
        return context
    
def index(request):
    return render(request, "dogruns/index.html")


def dogrun_list(request):
    dogruns = DogRun.objects.all()
    return render(request, "dogrun_list.html", {
        "dogruns": dogruns
    })

def dogrun_detail(request, pk):
    dogrun = get_object_or_404(DogRun, pk=pk)
    return render(request, "dogrun_detail.html", {
        "dogrun": dogrun
    })
    