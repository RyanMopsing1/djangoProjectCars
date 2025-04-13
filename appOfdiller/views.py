from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import ArticleForm, ArticleForm2, PoiskForm

from django.http import HttpResponseBadRequest

# Create your views here.
def index(request):
     news= News.objects.all()

     error = ' '
     if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
               if request.POST.get("prover"):
                    form.save()
                    return redirect('index')
               else:
                    error = 'Не согласована обработка персональных данных'
          else:
               error = 'Неверный формат'
     form = ArticleForm(request.POST)
     data = {'news':news, 'form':form, 'error':error}

     return render(request, 'index.html',data)






def models(request):
     return render(request, 'appOfdiller/modelryad_list.html')




class vnalichii(generic.ListView):
     model = Cars
     template_name = 'appOfdiller/cars_list.html'
     def get_context_data(self, **kwargs):
          data = super().get_context_data(**kwargs)
          data['myform'] = PoiskForm()
          return data

     def post(self, request, *args, **kwargs):
          if request.POST:
               k1 = request.POST['modeli']
               k2 = request.POST['cvet']
               k3 = request.POST['comp']
               if k1 and k2 and k3:
                    models = Cars.objects.filter(title_id=k1,cvet_id=k2,comp_id=k3)
               elif k1 and k2:
                    models = Cars.objects.filter(title_id=k1,cvet_id=k2)
               elif k1 and k3:
                    models = Cars.objects.filter(title_id=k1,cvet_id=k3)
               elif k2 and k3:
                    models = Cars.objects.filter(title_id=k2,cvet_id=k3)
               elif k1:
                    models = Cars.objects.filter(title_id=k1)
               elif k2:
                    models = Cars.objects.filter(cvet_id=k2)
               elif k3:
                    models = Cars.objects.filter(comp_id=k3)
               else:
                    models = []
               data = {
                    'models': models,
                    'myform': PoiskForm(request.POST),
                    'poisk':True
               }
               return render(request, self.template_name, data)
          else:
               data = {
                    'myform': PoiskForm(request.POST),
                    'poisk':False
               }
               return render(request, self.template_name, data)
class vladelcam(generic.ListView):
     model = Newsvlad

class pokup(generic.ListView):
     model = News
     template_name = 'appOfdiller/news_list.html'
     context_object_name = 'news_list'


     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['form'] = ArticleForm2()
          context['error'] = ' '
          return context

     def post(self, request, *args, **kwargs):
          form = ArticleForm2(request.POST)
          error= ' '
          if form.is_valid():
               if request.POST.get("prover"):
                    form.save()
                    return redirect('pokup')
               else:
                    error= 'Не согласована обработка персональных данных'
                    return render(request, 'appOfdiller/news_list.html',{'form':ArticleForm2(request.POST), 'error':error})
          else:
               error= 'Неверный формат'


          context = self.get_context_data()
          context['form'] = form
          context['error'] = error

          return render(request, self.template_name, context)


class modelryad(generic.ListView):
     model = ModelRyad



class modeldetail(generic.DetailView):
     model = ModelRyad

