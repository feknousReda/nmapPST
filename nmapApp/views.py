from django.views.generic import TemplateView
from django.shortcuts import render
from nmapApp.forms import HomeForm,SimpleForm,HomeFormOptions
from nmapApp.back import backProcess
import string

class HomeView(TemplateView):
    template_name = 'nmapApp/login.html'

    def get(self, request):
        form = HomeForm()
        form2 = HomeFormOptions()
        done = False
        args  = {'form': form,'form2': form2,  'done': done}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        form2 = HomeFormOptions(request.POST)


        if form.is_valid() and form2.is_valid():
            #if len(selected_modules) != 0:
            url = form.cleaned_data['Target']
            opt = form2.cleaned_data['Options']
            warning = ""
            try:
                backProcess.launchNmap(url,opt)
            except Exception as e:
                warning = "An exception appeared "+str(e)
                print("The warning is "+str(e))
            except ValueError:
                print("Value error has occured")
            #print("global process")
            form = HomeForm()
            form2 = HomeFormOptions()
            #print('executing')
            args = {'form': form,'form2':form2,'warning':warning}
            return render(request, self.template_name, args)
