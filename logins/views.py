from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from forms import InfoForm
from django.core.context_processors import csrf
from django.contrib import messages 
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView


from logins.models import Department, Info, Game, CustomUser
from django.contrib.auth.models import User, UserManager


#THIS VIEW SHOULD REPLACE THE CURRENT INDEX VIEW, BUT USER SHOULD FIRST BE GIVEN DEPARTMENT AND GAME
#VIEW THAT GIVES ACCESS TO THE INFO THAT THE USER IS PART OF

@login_required()
def index(request):
    u = request.user
    custom_user = CustomUser.objects.get(user=u)
    info_list =Info.objects.filter(game__in=custom_user.game.all(), department__in = custom_user.department.all()).distinct()
    #visible = Info.objects.filter(department__in=customuser.departments.all(), game__in=customuser.games.all())
    context = RequestContext(request, {
        'info_list': info_list,
    })
    template = loader.get_template('logins/index.html')

    args = {}
    args.update(csrf(request))
    
    args['index'] = Info.objects.all()
    return HttpResponse(template.render(context), args) 
    
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/logins/register_success')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('logins/register.html', args)

def register_success(request):
    return render_to_response('logins/register_success.html')

#VIEW TO DISPLAY THE NAME AND THE PASSWORD OF THE Info
def detail(request, info_id):
    info_details = Info.objects.get(id = info_id)
    template = loader.get_template('logins/details.html')
    context = RequestContext(request, {
        'info_details': info_details,
        })
    return HttpResponse(template.render(context))

def create(request):
    if request.POST:
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()
        
            messages.add_message(request, messages.SUCCESS, "Your Information was added")
            
            return HttpResponseRedirect('/logins')
    else:
        form = InfoForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('logins/create_info.html', args)

def delete_info(request, info_id):
    info_delete = Info.objects.get(id = info_id)
    template = loader.get_template('logins/delete.html')
    info_delete.delete()
    context = RequestContext(request, {
        'info_delete': info_delete,
        })
    return HttpResponse(template.render(context))


class InfoEdit(UpdateView):
    model = Info
    queryset = Info.objects.all()

def search_infos(request):
    infos = []
    if request.method == 'POST':    
        search_text = request.POST['search_text']
        u = request.user
        custom_user = CustomUser.objects.get(user=u)
        infos = Info.objects.filter(organization_name__contains = search_text, game__in=custom_user.game.all(), department__in = custom_user.department.all()).distinct()
    return render_to_response('logins/ajax_search.html', {'infos' : infos})




'''
#view
def edit_info(request, info_id):
    if request.method == 'POST':
        info = Info.objects.get(id=info_id)
        form = EditInfo(request.POST,instance=info)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.is_active = True
            info.save()
            return render_to_response('logins/edit.html', args)
        else:
            info = Info.objects.get(id=info_id)
            form = EditInfo(instance=info )
            return render_to_response('forsale.html', locals(), context_instance=RequestContext(request))

'''

'''
def detail(request, department_id):
    return HttpResponse("You're looking at department %s." % department_id)


def games(request, department_id):
    return HttpResponse("You're looking at the games of department %s." % department_id)
'''

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

'''
#VIEW TO GIVE ALL INFO IN THE DATABASE
def index(request):
    #if user_logged_in:
        info_list = Info.objects.all().order_by('-organization_name')[:100]
        template = loader.get_template('logins/index.html')
        context = RequestContext(request, {
            'info_list': info_list,
        })
        return HttpResponse(template.render(context))
    #else:
        #return HttpResponse('<h1>You must login</h1>')
'''