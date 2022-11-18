from django.http import JsonResponse


def students(request):
    if request.method == 'GET':
        students = {'id': 1, 'name': 'Joao'}
        return JsonResponse(students)

# Create your views here.
