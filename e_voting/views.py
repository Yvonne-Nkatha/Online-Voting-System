from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def test_view(request):
    return render(request, 'voting/test.html', {})

def logoutTest_view(request):
    logout(request)
    return redirect('test')  

#@login_required
def home_view(request):
    return render(request, 'voting/main.html', {})  

def find_user_view(request):
    #if able to find user
    return JsonResponse({'success': True})
       