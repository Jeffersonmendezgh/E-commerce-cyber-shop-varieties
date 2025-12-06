from django import forms
from .models import Auth


class FormRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ #widget = oculta el texto en el campo input
        'placeholder':'Ingresar Contraseña',
        'class': 'form-control',
    }))

    confirmar_password = forms.CharField(widget=forms.PasswordInput(attrs={ #attrs = atributos
        'placeholder':'Confirmar Contraseña',
        'class': 'form-control',
    }))
    class Meta: #metadatos del formulario de la clase Auth
        model= Auth
        fields=['name','lastname','email','phone_number','password'] #personalizacion de campos
    

    def __init__(self, *args,**kwargs):#init metodo constructor, **args= argumentos
        super(FormRegister,self).__init__(*args,**kwargs)#constructor de clase padre
        self.fields['name'].widget.attrs['placeholder']= 'ingresar Nombre' #metodo self = de el , el nombre,,,
        self.fields['lastname'].widget.attrs['placeholder']= 'Ingresar Apellido'
        self.fields['email'].widget.attrs['placeholder']= 'ingresar Email'
        self.fields['phone_number'].widget.attrs['placeholder']= 'ingresar Telefono'
        for field in self.fields:#por campo en campos del form agregar la [class]
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):#clean = validaciones personalizadas limpias en cada campo
        limpiar_datos= super(FormRegister, self).clean()#realizar validacioones automaticas y luego guardar datos limpios
        password= limpiar_datos.get('password')#primero valida, password clean
        confirmar_password= limpiar_datos.get('confirmar_password')#

        if password != confirmar_password:# si password no es igual, lanzar error
            raise forms.ValidationError(
                "Ups las contraseñas no Coinciden!"
            )
        


