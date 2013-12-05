from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from logins.models import Department, Info, Game, CustomUser
from django.contrib.auth.models import User, UserManager

'''
#THIS VIEW SHOULD REPLACE THE CURRENT INDEX VIEW, BUT USER SHOULD FIRST BE GIVEN DEPARTMENT AND GAME
#VIEW THAT GIVES ACCESS TO THE INFO THAT THE USER IS PART OF
def visible_info(request):
    visible = Info.objects.filter(department__in=customuser.departments.all(), game__in=customuser.games.all())
    context = RequestContext(request, {
        'visible': visible,
    })
    template = loader.get_template('logins/index.html')
    return HttpResponse(template.render(context)) 

'''
#VIEW TO GIVE ALL INFO IN THE DATABASE
def index(request):
    info_list = Info.objects.all().order_by('-organization_name')[:5]
    template = loader.get_template('logins/index.html')
    context = RequestContext(request, {
        'info_list': info_list,
    })
    return HttpResponse(template.render(context))

#VIEW TO DISPLAY THE NAME AND THE PASSWORD OF THE Info
def detail(request, info_id):
    info_details = Info.objects.get(id = info_id)
    template = loader.get_template('logins/details.html')
    context = RequestContext(request, {
        'info_details': info_details,
        })
    return HttpResponse(template.render(context))

'''
def detail(request, department_id):
    return HttpResponse("You're looking at department %s." % department_id)
'''

def games(request, department_id):
    return HttpResponse("You're looking at the games of department %s." % department_id)


'''
//CUTOM LOGIN USER (NOT USING RIGHT NOW AS BUILT-IN LOGIN IS BEING USED)

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

    return render_to_response('auth.html',{'state':state, 'username': username},
                                 context_instance=RequestContext(request))
'''

'''
#VIEW TO GIVE ALL INFO IN THE DATABASE
def index(request):
    latest_department_list = Department.objects.all().order_by('-name')[:5]
    template = loader.get_template('logins/index.html')
    context = RequestContext(request, {
        'latest_department_list': latest_department_list,
    })
    return HttpResponse(template.render(context))
'''