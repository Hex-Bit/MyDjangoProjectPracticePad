from django.shortcuts import render
from SecondApp.models import User
# Create your views here.

def index(request):
    return render(request,'SeconApp/index.html')


def users(request):
    users_list=User.objects.order_by('first_name')
    users_dict={'users':users_list}
    return render(request,'SecondAp/users.html',context=users_dict)