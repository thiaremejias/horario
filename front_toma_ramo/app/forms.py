from django import forms

class ValidarUsuario(forms.Form):
    email = forms.EmailField()
    contraseña = forms.CharField()

class Horario(forms.Form):
    id_asignatura = forms.IntegerField()
    ramos = forms.CharField()
   
   
   
   
   
   
   

    #IntegerField()
#CharField()