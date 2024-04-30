from django.shortcuts import redirect, render

from .forms import CreateUserForm




def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid(): 

            user = form.save()

            user.is_active = False

            user.save()





    context = {'form':form}


    return render(request, 'account/registration/register.html', context=context)


















