from django.shortcuts import render, redirect
from app.models import Profesor
from app.forms import ProfesorForm

# Create your views here.
def inicio(request):
    return render(request,'inicio.html',{})

def menu(request):
    return render(request,'menu.html',{}) 

# Manejo de profesores

def profesorNew(request):
    print("Llegue a NEW")
    form = ProfesorForm(request.POST)
    print(form)
    if form.is_valid():
        try:
            form.save()
            return redirect('/showprofesor')
        except:
            pass
    else:
        form = ProfesorForm
    return render(request,'profesorNew.html',{'form':form})

def profesorShow(request):
        profesor = Profesor.objects.all()
        return render(request,'profesorShow.html',{'profesor':profesor})

def profesorEdit(request, idprofesor):
        profesor = Profesor.objects.get(idprofesor = idprofesor)
        return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorUpdate(request, idprofesor):
        profesor = Profesor.objects.get(idprofesor = idprofesor)
        form = ProfesorForm(request.POST,intance=profesor)
        if form.is_valid():
            form.save()
            return redirect("/showprofesor")
        return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorDestroy(request, idprofesor):
        profesor = Profesor.objects.get(idprofesor = idprofesor)
        profesor.delete()
        return redirect("/showprofesor")

from django.shortcuts import render, redirect
from app.models import Materia
from app.forms import MateriaForm

#Manejo de materias

def materiaNew(request):
    print("Llegue a NEW")
    form = MateriaForm(request.POST)
    print(form)
    if form.is_valid():
        try:
            form.save()
            return redirect('/showmateria')
        except:
            pass
    else:
        form = MateriaForm
    return render(request,'materiaNew.html',{'form':form})

def materiaShow(request):
        materia = Materia.objects.all()
        return render(request,'materiaShow.html',{'materia':materia})

def materiaEdit(request, idmateria):
        materia = Materia.objects.get(idmateria = idmateria)
        return render(request,'materiaEdit.html',{'materia':materia})

def materiaUpdate(request, idmateria):
        materia = Materia.objects.get(idmateria = idmateria)
        form = MateriaForm(request.POST,intance=materia)
        if form.is_valid():
            form.save()
            return redirect("/showmateria")
        return render(request,'materiaEdit.html',{'materia':materia})

def materiaDestroy(request, idmateria):
        materia = Materia.objects.get(idmateria = idmateria)
        materia.delete()
        return redirect("/showmateria")
