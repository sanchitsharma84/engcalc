from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

def home4all(request):
    return render(request, 'user_app/home_for_all.html')

def get_data(request, *args, **kwargs):
    labels=["a", "b", "c", "d", "e"]
    default_items=[2, 4, 7, 4, 5]
    data  = {
        "labels":labels,
        "default":default_items,

    }
    return JsonResponse(data)


@login_required
def home4users(request):
    return render(request, 'user_app/home_for_reg_users.html')

# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         labels=[0, 1, 2, 3, 4]
#         default_items=[0, 1, 4, 9, 16]
#         data  = {
#             "labels":labels,
#             "default":default_items

#         }
#         return Response(data)