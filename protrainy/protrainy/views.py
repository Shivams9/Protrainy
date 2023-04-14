from django.shortcuts import render, HttpResponse


def test(request):
    return HttpResponse("Django Checked")


def user(request):
    user_name = "Shivam Singh"
    user_id = "124"
    user_branch = "MCA"
    user_address = "panjab"
    return render(request, 'user.html', {"user_name": user_name, "user_id": user_id, "user_branch":user_branch,"user_address": user_address})

