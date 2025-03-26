
from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import ArticleForm

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
     form = ArticleForm()
     data = {'news':news, 'form':form, 'error':error}

     return render(request, 'index.html',data)






def models(request):
     return render(request, 'appOfdiller/modelryad_list.html')




class vnalichii(generic.ListView):
     model = Cars


class vladelcam(generic.ListView):
     model = Newsvlad

class pokup(generic.ListView):
     model = News

class modelryad(generic.ListView):
     model = ModelRyad

class modeldetail(generic.DetailView):
     model = ModelRyad

