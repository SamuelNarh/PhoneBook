from django.shortcuts import render,redirect
from . models import PhoneBook

# Create your views here.
def index(request):  
    contacts=PhoneBook.objects.all()
    if request.method == 'GET':
      search = request.GET.get("search")
      if search!=None:
        contacts= contacts.filter(lastname__icontains=search)
    context={'contacts':contacts} 
    return render(request,"index.html",context)


def add(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname= request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        contacts = PhoneBook(firstname=firstname,lastname=lastname,mobile_number=phonenumber)
        contacts.save()
        return redirect('index')
    return render(request,"add.html")

def edit(request,pk):
    contacts=PhoneBook.objects.get(id=pk)
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname= request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        contacts = PhoneBook(id=pk,firstname=firstname,lastname=lastname,mobile_number=phonenumber)
        contacts.save()
        return redirect('index')
    context={'contacts':contacts}
    return render(request,"edit.html",context)

def delete(request,pk):
    contacts=PhoneBook.objects.get(id=pk)
    contacts.delete()
    return redirect('index')