from rest_framework.response import Response
from rest_framework.decorators import api_view
from CPLN.models import *
from .serializers import *
from django.http.response import JsonResponse



'''@api_view(['GET'])
def getUserPage(request):
    users = Userpage.objects.all()
    serializer = UserPageSerializer(users, many=True)
    return Response(serializer.data)'''

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

@api_view(['GET', 'POST'])
def Neighborhoods(request):
    if request.method == 'POST':
        serializeobj = Neighborhood(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response("Person created")
        else:
            return Response("Invalid Person")
    else:
        users = Neighborhood.objects.all()
        serializer = Neighborhood(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def MyNotices(request):
    notices = DailyCard.objects.all()
    serializer = DailyCardSerializer(notices, many=True)
    return Response(serializer.data)
    
@api_view(['PUT', 'POST','DELETE'])
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
        newNotice = DailyCardSerializer(data=request.data)
        if newNotice.is_valid():
            newNotice.save()
            return Response("Notice created")
        return Response(newNotice.errors)

    elif request.method == 'DELETE':
        myNotice = DailyCard.objects.filter(pk=pk).first()
        if myNotice != None:
            myNotice.delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Notice not found..."}
        return JsonResponse(datos)


@api_view(['GET'])
def MyList(request):
    notices = ListFood.objects.all()
    serializer = ListFoodSerializer(notices, many=True)
    return Response(serializer.data)