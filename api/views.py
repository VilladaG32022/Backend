from rest_framework.response import Response
from rest_framework.decorators import api_view
from CPLN.models import *
from .serializers import *
import json
from django.http.response import JsonResponse

from rest_framework.views import APIView


@api_view(['GET'])
def getUserPage(request):
    users = Userpage.objects.all()
    serializer = UserPageSerializer(users, many=True)
    return Response(serializer.data)


'''class ToVolunteer(APIView):
    def put(self, request, pk):
        jd = json.loads(request.body)
        persons = list(Person.objects.filter(pk=pk).values())
        if len(persons) > 0:
            person = Person.objects.get(pk=pk)
            person.is_candidate = False
            person.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def Delete(self, request, pk):
        if request.method == 'DELETE':
            #jd = json.loads(request.body)
            person = Person.objects.filter(pk=pk).first()
            if person != None:
                person.delete()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)

    def post(self, request, pk):
        serializeobj = PersonSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response("Person created")
        return Response(serializeobj.errors)'''


'''class PersonTable(APIView):
    def get(self, request):
        users = Person.objects.all()
        serializer = PersonSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializeobj = PersonSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response("Person created")
        return Response(serializeobj.errors)'''

@api_view(['GET', 'POST'])
def inscriptions(request):
    if request.method == 'POST':
        serializeobj = PersonSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response("Person created")
        else:
            return Response("Invalid Person")
    else:
        users = Person.objects.all()
        serializer = PersonSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT', 'POST','DELETE'])
def notices(self, request, pk):
    if request.method == 'PUT':
        images = list(DailyCard.objects.filter(pk=pk).values())
        if len(images) > 0:
            serializeobj=DailyCardSerializer(images,data=request.data)
            if serializeobj.is_valid():
                serializeobj.save()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Bad request..."}
        else:
            datos = {'message': "Notice not found..."}
        return JsonResponse(datos)

    elif request.method == 'POST':
        newExpo = DailyCard.objects.all(data=request.data)
        if newExpo.is_valid():
            newExpo.save()
            return Response("Notice created")
        return Response(newExpo.errors)

    elif request.method == 'DELETE':
        myExpo = DailyCard.objects.filter(pk=pk).first()
        if myExpo != None:
            myExpo.delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Notice not found..."}
        return JsonResponse(datos)
    else:
        notices = DailyCard.objects.all()
        serializer = DailyCardSerializer(notices, many=True)
        return Response(serializer.data)
