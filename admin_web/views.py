from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

def ingresar(request):  
    """vista para poder ingresar a la pagina""" 


    return render(request, 'admin_web/login.html')
    """ 
    if request.method == 'POST': 
        control = request.POST.get('control')
        psword  = request.POST.get('psword')
        
        #control = '317484'
        #psword  = '121212'        
        
        usuario = authenticate(control = control, password = psword)
        if usuario:
            login(request, usuario)

            messages.success(request, 'A ingresado correctamente')
            return redirect('index')
            
        
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html') """

