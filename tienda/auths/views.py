from django.shortcuts import render,redirect
from .forms import FormRegister
from .models import Auth
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def login_view(request):
    if request.method == "POST":#si el metodo de respuesta es post,
        email = request.POST["email"]# si en input viene email y password
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)#nos logeamos
            return redirect("home:home")#lo enviamos al menu
        else: 
            messages.error(request, "password incorrecto")#si algo falla
            return redirect ("auths:login")#devolvemos al login redireccionando url
    return render(request, "auths/login.html")#aca redireccionamos al archivo html

def logout_view(request):
    auth.logout(request)
    messages.success(request, "has salido con exito")
    return render(request, "auths/login.html")#que devuelva al login

    
def signing_view(request):
    if request.method == "POST": #ingreso de datos
        form = FormRegister(request.POST) #variable que hereda de formregister
        if form.is_valid():
            name = form.cleaned_data["name"]# tomamos todos estos datos
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            phone_number = form.cleaned_data["phone_number"]
        
            username = email.split("@")[0]# nombre de usuario, le decimos que sera el email, [0]para que parta desde el inicio @=que se genere usuario con lo que esta antes del @
            user = Auth.objects.create_user( #metodo que hereda de auth
                name = name,
                lastname = lastname,
                username = username,
                email = email,
                password = password,
                )
            user.phone_numer = phone_number
            user.save() #save en db
            current_site = get_current_site(request)#obtener el dominio del sitio
            body_email = "Hola activa tu cuenta para poder ingresar" #cuerpo para mensaje
            message = render_to_string("auths/verify_account.html", {#render_to_string =comvertir plantilla a texto 
                "user":user, #mensaje dirijido al user
                "domain":current_site, #dominio sitio actual
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),# urlsafe_base_encode=id  user.pk=obtengo la primera key del usuario y force= cpmvertir el id en hash
                "token": default_token_generator.make_token(user), #token unico de activacion para el usuario
            }) 
            asunto= 'activa tu cuenta codelatin'
            text_message = strip_tags(message)

            send_email = EmailMultiAlternatives(
                subject=asunto,
                body=text_message,
                to=[email]
            )
            send_email.attach_alternative(message, "text/html")
            send_email.send()
            
            return redirect("auths:signing")


    else:
        form = FormRegister()

    context = {
        "form": form,
    }

    return render(request,"auths/register.html", context=context)

def activate_account(request, uidb64, token):
    try:
        uid= urlsafe_base64_decode(uidb64).decode()
        user=Auth._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Auth.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        messages.success(request, 'Felicitaciones Tu Cuenta Ha sido Activada!')
        return redirect('auths:login')
    else:
        messages.error(request, 'Ups no se ha podido Validar la cuenta')
        return redirect('auths:registro')
    
    ##return render: para renderizar plantillas, si necesita una resquest como parametro
    ###return redirect: redirecciona vistas, no necesita un request, funciona similar a la tag a, solo renderiza una vista