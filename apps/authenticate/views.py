from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apps.blackList.models import BlackList
from ipware import get_client_ip

# Create your views here.
def mylogin(request):

    if request.method == 'POST' :
        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')
        if utxt != "" and ptxt != "" :
            user = authenticate(username=utxt, password=ptxt)
            if user != None :
                ip, is_routable = get_client_ip(request)
                if ip is None :
                    ip = "0.0.0.0"
                b = len(BlackList.objects.filter(ip=ip))
                if b != 0 :
                    msg = "Your ip Blocked By Admin"
                    return render(request, 'front/msgbox.html', {'msg':msg})

                login(request, user)
                return redirect('panel')
    return render(request, 'authenticate/login.html')