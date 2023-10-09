from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from appCoder.forms import *
from appCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_req(request):
    
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = password)

            if user:

                login(request, user)

                return render(request, "appCoder/inicio.html", {"mensaje":f"Bienvenido {user}"})
            
        else:

            return render(request, "appCoder/inicio.html", {"mensaje":"Datos incorrectos"})

    else:

        form = AuthenticationForm()

    return render(request, "appCoder/login.html",{"formulario":form})

def registro(request):

    if request.method == "POST":

        form = user_signup(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "appCoder/inicio.html",{"mensaje":"Usuario creado con éxito"})
        
    else:

        form = user_signup()
    
    return render(request, "appCoder/signup.html", {"formulario": form})

@login_required
def inicio(request):

    return render(request,"appCoder/inicio.html")

def item(request):

    if request.method == "POST":

        formItem = ItemsForm(request.POST)

        if formItem.is_valid():

            info = formItem.cleaned_data

            obj = Item(title=info["title"], description=info["description"], price=info["price"])

            obj.save()         

            return render(request, "appCoder/inicio.html")
    
    else:
        formItem = ItemsForm()
    
    return render(request,"appCoder/item.html", {"form_item":formItem})

@login_required
def update_user(request):

    usuario = request.user

    if request.method == "POST":

        form = updateForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.save()

            return render(request, "appCoder/inicio.html",{"mensaje":"Usuario actualizado con éxito"})
    else:

        form = updateForm(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
        })
    
    return render(request, "appCoder/updateProfile.html", {"formulario":form, "usuario":usuario})


@login_required
def agregar_avatar(request):

    if request.method=="POST":

        form = avatarForm(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "appCoder/inicio.html", {"mensaje":"Avatar actualizado con éxito"})

    else:

        form = avatarForm()
    
    return render(request, "appCoder/addAvatar.html", {"formulario":form})


def about(request):
    
    return render(request,"appCoder/about.html")


@login_required
def categoria(request):
    
    if request.method == "POST":

        form = CategoriaForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            cat = Categ(name=info["name"], description=info["description"])

            cat.save()         

            return render(request, "appCoder/inicio.html")
    
    else:
        form = CategoriaForm()
    
    return render(request,"appCoder/categoria.html", {"form_cat":form})

@login_required
def busquedaCateg(request):
    
    return render(request,"appCoder/categoria.html")

@login_required
def mostrarCateg(request):

    if request.GET["busqueda_categ"]:

        categoria = request.GET["busqueda_categ"]
        cat = Categ.objects.filter(name__icontains=categoria)
        print("cat",cat)
        print("categoria",categoria)
        return render(request, "appCoder/categoria.html", {"categorias":cat, "busqueda_categ":categoria})

    else:

        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

@login_required
def tecnologia(request):
    
    return render(request,"appCoder/tecnologia.html")

@login_required
def muebles(request):
    
    return render(request,"appCoder/muebles.html")

@login_required
def cocina(request):
    
    return render(request,"appCoder/cocina.html")

@login_required
def decoracion(request):
    
    return render(request,"appCoder/decoracion.html")

@login_required
def readItems(request):

    items = Item.objects.all()

    context = {"items":items}

    return render(request, "appCoder/readItems.html", context)

class ListItems(LoginRequiredMixin, ListView):

    model = Item

class DetailItems(LoginRequiredMixin, DetailView):

    model = Item

class CreateItems(LoginRequiredMixin, CreateView):

    model = Item
    success_url = "/appCoder/items/list"
    fields = ["title","price","description","created_date","condition","category","image"]
    
class UpdateItems(LoginRequiredMixin, UpdateView):

    model = Item
    success_url = "/appCoder/items/list"
    fields = ["title","price","description","created_date","condition","category","image"]

class DeleteItems(LoginRequiredMixin, DeleteView):

    model = Item
    success_url = "/appCoder/items/list"


class ListItemsCocina(LoginRequiredMixin, ListView):

    model = Item

    def get_queryset(self) -> QuerySet[Any]:
        return Item.objects.filter(category=3)

class ListCat(LoginRequiredMixin, ListView):

    model = Categ

class DetailCat(LoginRequiredMixin, DetailView):

    model = Categ

class CreateCat(LoginRequiredMixin, CreateView):

    model = Categ
    success_url = "/appCoder/category/list"
    fields = ["name","description"]
    
class UpdateCat(LoginRequiredMixin, UpdateView):

    model = Categ
    success_url = "/appCoder/category/list"
    fields = ["name","description"]

class DeleteCat(LoginRequiredMixin, DeleteView):

    model = Categ
    success_url = "/appCoder/category/list"
