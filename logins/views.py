from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm

from logins.models import Department, Info, Game, CustomUser

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
def login(request, template_name='login.html'):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.login(request):
            return redirect('/logins')
    else:
        form = LoginForm()
    return render_to_response(template_name, {'form': form,}, RequestContext(request))


'''
def login(request):
    email = ''
    password = ''
    state = "Please login below: "

    form = AuthenticationForm(data=(request.POST or None))

    if form.is_valid():
        # Since the USERNAME_FIELD in custom-user is the email, that is what
        # we expect as input to the username field of this form
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=email,password=password)

        if user is not None and user.is_active:
            login(request, login)
            state = "You have been logged in"
        else:
            state = "Invalid login credentials"

    t = loader.get_template('login.html')
    c = RequestContext(request, {'state': state, 'form': form})
    return HttpResponse(t.render(c))
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