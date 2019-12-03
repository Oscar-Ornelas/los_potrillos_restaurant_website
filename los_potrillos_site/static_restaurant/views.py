from django.shortcuts import render, redirect
from static_restaurant.forms import PostForm
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class Menu(TemplateView):
    template_name = 'menu.html'

class Location(TemplateView):
    template_name = 'location.html'

def contact_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('static_restaurant:contact_form')
    else:
        form = PostForm()
    return render(request, 'contact.html', {'form': form})
