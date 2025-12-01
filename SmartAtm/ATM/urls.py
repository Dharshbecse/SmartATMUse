from django.urls import path
from . import views
from .views import *

urlpatterns = [
      path('pin/',PinNumGetPost.as_view()),
      path('profile/',Profile.as_view()),
      path('profile/',Account.as_view()),
      path('language/',views.All_language, name="language"),
      path('transaction/',views.Transaction,name="transaction"),
      path('account_type/',views.Account_type,name="account_type"),
      path('pin_enter/<int:atm_pin_num_id>/',views.Pin,name="pins"),
      path('withdraw/',views.withdraw,name="withdraw"),
      path('withdraw/',views.withdrawTamil,name="withdraw_tamil"),
      path('pin_change/<int:atm_pin_num_id>/',views.PinChanging,name="pins_change"),
      path('deposit/',views.Deposit,name="deposit"),
      path('account_type_d/',views.Account_Type_d,name="account_type_d"),
      path('pin_num_d/<int:atm_pin_num_id>/',views.Pin_Num_d,name="pin_num_d"),
      path('pin_num_t/<int:atm_pin_num_id>/',views.Pin_Num_t,name="pin_num_t"),
      path('transfer_amount/',views.Transfer_Amount,name="transfer_amount"),
      path('transfer/',views.Transfer,name="transfer"),

      #tamil
      path('transactionT/',views.TransactionTamil,name="transactionT"),
      path('withdrawT/',views.withdrawTamil,name="withdrawT"),
      path('account_typeT/',views.Account_typeTamil,name="account_typeT"),
      path('pin_enterT/<int:atm_pin_num_id>/',views.PinTamil,name="pinsT"),
      path('withdrawT/',views.withdrawTamil,name="withdrawT"),
      path('pin_changeT/<int:atm_pin_num_id>/',views.PinChangingTamil,name="pins_changeT"),
      path('depositT/',views.DepositTamil,name="depositT"),
      path('account_type_dT/',views.Account_Type_dTamil,name="account_type_dT"),
      path('pin_num_dT/<int:atm_pin_num_id>/',views.Pin_Num_dTamil,name="pin_num_dT"),
      path('pin_num_tT/<int:atm_pin_num_id>/',views.Pin_Num_tTamil,name="pin_num_tT"),
      path('transfer_amountT/',views.Transfer_AmountTamil,name="transfer_amountT"),
      path('transferT/',views.TransferTamil,name="transferT"),


      ]