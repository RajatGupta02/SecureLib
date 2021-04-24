from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Book , IssueRequest, Approval
from math import ceil
from .forms import BookForm, IssueForm
from datetime import datetime, timedelta


# Create your views here.
# def index(request):
#     if request.user.is_authenticated:
#         return render(request, 'librarymanager/index.html')
#     return redirect('/login')
    
def loginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/libview")
        
        else:
            return render(request, 'librarymanager/login.html')
    
    return render(request, 'librarymanager/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/libview")
    else:
        form=UserCreationForm()
    
    return render(request,"librarymanager/register.html",{"form":form})

def libview(request):
    books= Book.objects.all()
      
    boollist=[]
    boollistnew=[]

    for bks in books:
        boollist.append(Approval.objects.filter(student_id=request.user.id,book_name=bks.book_name))
        boollistnew.append(IssueRequest.objects.filter(student_id=request.user.id,book_name=bks.book_name))
    n=len(books)
    nSlides= n//4 + ceil((n/4) - (n//4)) + 1
    params = {'range': range(nSlides),'books': books, 'boollist': boollist , 'boollistnew': boollistnew}
    if request.user.is_authenticated:
        return render(request, 'librarymanager/libview.html',params)
    return redirect('/login')

def bookview(request,id):
    if request.user.is_authenticated:
        book = Book.objects.filter(id=id)
        books= Book.objects.all()
        boollist=[]

        for bks in books:
            boollist.append(IssueRequest.objects.filter(student_id=request.user.id,book_name=bks.book_name))
        params={'book':book[0],'books':books, 'boollist':boollist}
        return render(request, 'librarymanager/bookview.html',params)
        # return render(request, 'librarymanager/bookview.html',{'book':book[0]})
    return redirect('/login')

def profileview(request,id):
    if request.user.is_authenticated:
        profile = request.user.id
        return render(request, 'librarymanager/profileview.html',{'profile': profile})
    return redirect('/login')

def managebooks(request):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
        books= Book.objects.all()
        n=len(books)
        nSlides= n//4 + ceil((n/4) - (n//4)) + 1
        params = {'range': range(nSlides),'books': books}
        if request.user.is_authenticated:
            return render(request, 'librarymanager/managebooks.html',params)
        return redirect('/login')
    else:
        return redirect('/libview')

def addbook(request):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
    
        bookform= BookForm()
        if request.method =='POST':
            bookform = BookForm(request.POST, request.FILES)
            if bookform.is_valid():
                bookform.save()
                return redirect("/managebooks")
        context = {'bookform': bookform}
        return render(request, 'librarymanager/addbook.html',context)
    else:
        return redirect('/libview')

def editbook(request,pk):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
        reqbook = Book.objects.get(id=pk)
        bookform= BookForm(instance=reqbook)
        if request.method =='POST':
            bookform = BookForm(request.POST, request.FILES, instance=reqbook)
            if bookform.is_valid():
                bookform.save()
                return redirect("/managebooks")
        context = {'bookform': bookform}
        return render(request, 'librarymanager/addbook.html',context)
    else:
        return redirect('/libview')

def deletebook(request,pk):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
        reqbook = Book.objects.get(pk=pk)
        if request.method =='POST':
            reqbook.delete()
            return redirect("/managebooks")
            context = {'reqbook': reqbook}
            return render(request, 'librarymanager/managebooks.html',context)
    else:
        return redirect('/libview')

def issuebook(request,bookname,stid):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()
     
    if request.user not in users_in_group:
        if request.method=="POST":
            student_name= request.POST.get('student_name', '')
            email=request.POST.get('email', '')
            duration=request.POST.get('duration', '8')
            phone=request.POST.get('phone', '')
            issuerequest = IssueRequest(book_name= bookname, student_name=student_name, student_id= stid ,duration=duration , email=email,phone=phone)
            
            issuerequest.save()
            
            # id=issuerequest.request_id
            return render(request, 'librarymanager/success.html')
        return render(request, 'librarymanager/issuebook.html')
        # else:
        #     return redirect('/libview')
    else:
        return redirect('/libview')

def viewrequests(request):
    issuedbooks=IssueRequest.objects.all()
    temp=[]
    for ibook in issuedbooks:
        idate=str(ibook.date.day)+'-'+str(ibook.date.month)+'-'+str(ibook.date.year)
        
        
        books=list(Book.objects.filter(book_name=ibook.book_name))
        students=list(IssueRequest.objects.filter(student_name=ibook.student_name))
        
        
        j=0
        for bk in books:
            t=(ibook.request_id,ibook.book_name,students[j],ibook.student_id,ibook.email,idate, ibook.duration)
            j=j+1
            temp.append(t)

    return render(request,'librarymanager/viewrequests.html',{'temp':temp})

def deleterequest(request,request_id):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
        reqrequest = IssueRequest.objects.get(request_id=request_id)
        if request.method =='POST':
            reqrequest.delete()
            return redirect("/viewrequests")
            context = {'reqrequest': reqrequest}
            return render(request, 'librarymanager/viewrequests.html',context)
    else:
        return redirect('/libview')
def approverequest(request,request_id):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
        reqrequest = IssueRequest.objects.get(request_id=request_id)
        if request.method =='POST':
            student_name=reqrequest.student_name
            book_name=reqrequest.book_name
            stid=reqrequest.student_id
            email=reqrequest.email
            duration=reqrequest.duration
            phone=reqrequest.phone
            approval = Approval(book_name= book_name, student_name=student_name, student_id= stid ,duration=duration , email=email,phone=phone)
            approval.save()

            
            chngqty=Book.objects.get(book_name=book_name)
            chngqty.quantity-=1
            chngqty.save()
            
            reqrequest.delete()
            return redirect("/viewrequests")
            context = {'reqrequest': reqrequest}
            return render(request, 'librarymanager/viewrequests.html',context)
    else:
        return redirect('/libview')

def viewapproved(request):
    approverequests=Approval.objects.all()
    temp=[]
    for ibook in approverequests:
        idate=str(ibook.approvaldate.day)+'-'+str(ibook.approvaldate.month)+'-'+str(ibook.approvaldate.year)
        
        
        books=list(Book.objects.filter(book_name=ibook.book_name))
        students=list(Approval.objects.filter(student_name=ibook.student_name))
        
        
        j=0
        for bk in books:
            t=(ibook.request_id,ibook.book_name,students[j],ibook.student_id,ibook.email,idate, ibook.duration)
            j=j+1
            temp.append(t)

    return render(request,'librarymanager/viewapprovedrequests.html',{'temp':temp})

def returned(request,request_id):
    users_in_group = Group.objects.get(name="Librarian").user_set.all()

    if request.user in users_in_group:
        reqrequest = Approval.objects.get(request_id=request_id)
        if request.method =='POST':
            reqrequest.delete()
            return redirect("/viewapprovedrequests")
            context = {'reqrequest': reqrequest}
            return render(request, 'librarymanager/viewapprovedrequests.html',context)
    else:
        return redirect('/libview')