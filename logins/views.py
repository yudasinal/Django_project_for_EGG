from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from forms import InfoForm
from django.core.context_processors import csrf
from django.contrib import messages 
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, UserManager
from django.core.mail import send_mail


from logins.models import Department, Info, Game, CustomUser
from django.contrib.auth.models import User, UserManager


#THIS VIEW SHOULD REPLACE THE CURRENT INDEX VIEW, BUT USER SHOULD FIRST BE GIVEN DEPARTMENT AND GAME
#VIEW THAT GIVES ACCESS TO THE INFO THAT THE USER IS PART OF

@login_required()
def index(request):
    u = request.user
    custom_user = CustomUser.objects.get(user=u)
    #if not custom_user.is_admin_approved == False:
        #return HttpResponseRedirect('/logins/register_success')
    try:
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

    except ObjectDoesNotExist:
        info_list = None;
        context = RequestContext(request, {
        'info_list': info_list,
        })
        template = loader.get_template('logins/index.html')
        args = {}
        args.update(csrf(request))
            
        args['index'] = Info.objects.all()
        return HttpResponse(template.render(context), args)
        

# Logout view
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

# Registering a user
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

# Successful regestration
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

# View to create a new information
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

# Deletion of information
def delete_info(request, info_id):
    info_delete = Info.objects.get(id = info_id)
    template = loader.get_template('logins/delete.html')
    info_delete.delete()
    context = RequestContext(request, {
        'info_delete': info_delete,
        })
    return HttpResponse(template.render(context))


# Editing an information
class InfoEdit(UpdateView):
    model = Info
    queryset = Info.objects.all()


# Searching the informations
def search_infos(request):
    infos = []
    if request.method == 'POST':    
        search_text = request.POST['search_text']
        u = request.user
        custom_user = CustomUser.objects.get(user=u)
        infos = Info.objects.filter(title__contains = search_text, game__in=custom_user.game.all(), department__in = custom_user.department.all()).distinct()
    return render_to_response('logins/ajax_search.html', {'infos' : infos})


