from django.shortcuts import render
from app.forms import *
import sys
import requests
import json

# Create your views here.
def list_ramos(request):
    print('find_all')
    url = 'http://localhost:3000/take_course'
    try:
        
        response = requests.get(url)
        print('status_code: {0}'.format(response.status_code))
        value = response.json()
        value_dumps = json.dumps(value)
        newvalue= json.loads(value_dumps)
        horarios = newvalue ["data"]
        print (horarios)
        return render(request, 'index.html',{'horarios':horarios})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))
    

def validar_usuario(request):
    print(request.method)
    
    if request.method == "POST":
        #url = 'http://localhost:3000/valid_user/{0}/{1}'.format(email,contraseña)
        try: 
            #url= url+request.POST['email'] + '/' + request.POST['contraseña']
            email = request.POST['email']
            contraseña = request.POST['contraseña']
            url = 'http://localhost:3000/valid_user/{0}/{1}'.format(email,contraseña)
            print('-----------')
            print(url)
            response = requests.get(url)
            print('status_code: {0}'.format(response.status_code))
            status = response.status_code

            if status == 200:
                value = response.json()
                value_dumps = json.dumps(value)
                usuario = json.loads(value_dumps)
                print (usuario)
                estado = usuario ['status']
                return render(request, 'usuario_validado.html', {'estado':estado})
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))
    else: 
        form = ValidarUsuario()
        return render(request, 'Validar_usuario.html', {'form':form})

def horario(request):
        print('horario')
        url = 'http://localhost:3000/take_course'
        if request.method == "POST":
            try:
                horario_json = {
                    'id_asignatura': int(request.POST['id_asignatura']), 
                    'ramos': request.POST['ramos'],
                   
                }
                response = requests.post(url, json=horario_json)
                print('status_code: {0}'.format(response.status_code))
                horario= response.json()
                print (horario)
                return redirect('/')
            except Exception as e:
                print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
        else:
            form = Horario()
            return render(request, 'Agregar_horario.html', {'form': form})

