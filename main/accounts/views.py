# Create your views here.
#from django import form
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import logout


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def profile(request):
    return render_to_response('accounts/profile.html', {'request': request}, context_instance=RequestContext(request))

def edit(request):
    return render_to_response('accounts/edit.html', {'request':request}, context_instance=RequestContext(request))

def save_edits(request):
    user = request.user
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return HttpResponseRedirect(reverse('accounts.views.profile'))

def logout(request):
    logout(request)
    return redirect('c2g.views.home')

@sensitive_post_parameters()
@csrf_protect
@never_cache
def register(request, template_name='accounts/register.html'):
    form=AuthenticationForm(request)
    t=loader.get_template(template_name)
    c=Context({
        'test': 'test',       
        'form': form,
    });
    return HttpResponse(t.render(c))

    

