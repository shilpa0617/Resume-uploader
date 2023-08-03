from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.shortcuts import redirect

# Create your views here.

class HomeView(View):
    def get(self , request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request , 'myapp/home.html' , {'candidates': candidates , 'form': form})
    
    def post(self , request):
        form = ResumeForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            # Redirect the user to the same URL after successful form submission
            return redirect('home')
        else:
            # If the form is not valid, render the form again with the validation errors
            return render(request, 'myapp/home.html', {'form': form})
        
class CandidateView(View):
    def get(self, request , pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html' , {'candidate': candidate})