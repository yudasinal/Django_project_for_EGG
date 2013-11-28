from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from logins.models import Department

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username})


def index(request):
    latest_department_list = Department.objects.all().order_by('-name')[:5]
    template = loader.get_template('logins/index.html')
    context = RequestContext(request, {
        'latest_department_list': latest_department_list,
    })
    return HttpResponse(template.render(context))

def detail(request, department_id):
    return HttpResponse("You're looking at department %s." % department_id)

def games(request, department_id):
    return HttpResponse("You're looking at the games of department %s." % department_id)


