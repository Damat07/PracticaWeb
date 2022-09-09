from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(self,name):
    return HttpResponse(f'Hola soy {name}')

def homePage(self):
    lista = [1,2,3,4]
    data = {'nombre':'David','apellido':'Toledo', 'lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    curso = Curso(nombre='UX/UI',camada=12345)
    curso.save()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documento)
