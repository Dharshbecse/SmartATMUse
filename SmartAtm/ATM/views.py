from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .Serializer import *


class PinNumGetPost(APIView):  
    def get(self,request):
        all__task=Pin_Num.objects.all()
        task_data=Pin_Num_Serializer(all__task,many=True).data
        return Response(task_data)
    def post(self,request):
        new_task=Pin_Num_Serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("new_task_added")
        else:
            return Response(new_task.errors)

class Profile(APIView):  
    def get(self,request):
        all__task=profile.objects.all()
        task_data=Profile_Serializer(all__task,many=True).data
        return Response(task_data)
    def post(self,request):
        new_task=Profile_Serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("new_task_added")
        else:
            return Response(new_task.errors)        
        
class Account(APIView):  
    def get(self,request):
        all__task=account.objects.all()
        task_data=Account_Serializer(all__task,many=True).data
        return Response(task_data)
    def post(self,request):
        new_task=Account_Serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("new_task_added")
        else:
            return Response(new_task.errors)    
def All_language(request):
        return render(request,'language.html') 


def Transaction(request):
        return render(request,'transaction.html')
def Account_type(request):
        return render(request,'account_type.html')

def Pin(request,atm_pin_num_id):
    log=Pin_Num.objects.get(pk=atm_pin_num_id)
    return render(request,'pin_num.html',{'pin':log})

def withdraw(request):
        return render(request,'withdraw.html')

def Account_typeTamil(request):
        return render(request,'account_type.html')



def withdrawTamil(request):
        return render(request,'withdraw.html')


def PinChanging(request, atm_pin_num_id):
    # Fetch PIN object by ID
    pin_num = Pin_Num.objects.get(id=atm_pin_num_id)

    return render(request, 'pin_change.html', {'pin_num': pin_num})      

def Deposit(request):
    return render(request,'deposit.html')

def Account_Type_d(request):
    return render(request,'account_type_d.html')

def Pin_Num_d(request,atm_pin_num_id):
    log=Pin_Num.objects.get(pk=atm_pin_num_id)
    return render(request,'pin_num_d.html',{'pin':log})

def Pin_Num_t(request,atm_pin_num_id):
    log=Pin_Num.objects.get(pk=atm_pin_num_id)
    return render(request,'pin_num_t.html',{'pin':log})

def Transfer_Amount(request):
    return render(request,'transfer_amount.html')


def Transfer(request):
    return render(request,'transfer.html')

# tamil


def TransactionTamil(request):
        return render(request,'tamil/transactionT.html')  

def PinTamil(request,atm_pin_num_id):
    log=Pin_Num.objects.get(pk=atm_pin_num_id)
    return render(request,'tamil/pin_numT.html',{'pin':log})

def Account_typeTamil(request):
        return render(request,'tamil/account_typeT.html')


def withdrawTamil(request):
        return render(request,'tamil/withdrawT.html')

def Account_typeTamil(request):
        return render(request,'tamil/account_typeT.html')



def withdrawTamil(request):
        return render(request,'tamil/withdrawT.html')


def PinChangingTamil(request, atm_pin_num_id):
    # Fetch PIN object by ID
    pin_num = Pin_Num.objects.get(id=atm_pin_num_id)

    return render(request, 'tamil/pin_changeT.html', {'pin_num': pin_num})      

def DepositTamil(request):
    return render(request,'tamil/depositT.html')

def Account_Type_dTamil(request):
    return render(request,'tamil/account_type_dT.html')

def Pin_Num_dTamil(request,atm_pin_num_id):
    log=Pin_Num.objects.get(pk=atm_pin_num_id)
    return render(request,'tamil/pin_num_dT.html',{'pin':log})

def Pin_Num_tTamil(request,atm_pin_num_id):
    log=Pin_Num.objects.get(pk=atm_pin_num_id)
    return render(request,'tamil/pin_num_tT.html',{'pin':log})

def Transfer_AmountTamil(request):
    return render(request,'tamil/transfer_amountT.html')


def TransferTamil(request):
    return render(request,'tamil/transferT.html')
