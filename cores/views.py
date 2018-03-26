# views.py 
from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
   return render(request, "index.html") 
   
def contato(request): 
   if request.method == "GET": 
      print ("Acesso via GET")
      return render(request, "contato.html") 
   else:
      print ("Acesso via POST| Nome: ", request.POST.get("nome"), " - E-mail:", request.POST.get("email"), " - Telefone:", request.POST.get("telefone"), " - CPF:", request.POST.get("cpf"), " - Sexo:", request.POST.get("sexo"), " - Data Nascimento:", request.POST.get("dtnasc"))
      return render(request, "index.html")

def login(request): 
   if request.method == "GET": 
      print ("Acesso via GET")
      return render(request, "login.html") 
   else:
      if request.POST['senha'] == "teste123":
         print ("Usuário: ", request.POST.get("email"), " entrou com sucesso!")
         return render(request, "index.html")
      else:  
         print ("Usuário: ", request.POST.get("email"), " digitou a senha errada!")
         return render(request, "login.html")
      