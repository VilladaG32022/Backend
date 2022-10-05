from rest_framework.response import Response
from rest_framework.decorators import api_view
from CPLN.models import *
from .serializers import *
from django.http.response import JsonResponse

@api_view(['GET', 'POST'])
def inscriptions(request):
    if request.method == 'POST':
        serializeobj = CandidateSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response("Candidate created")
        else:
            return Response("Invalid Candidate")
    else:
        users = Candidate.objects.all()
        serializer = CandidateSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def Neighborhoods(request):
    if request.method == 'POST':
        serializeobj = NeighborhoodSerializer(data=request.data, many=True)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response("Neighborhood created")
        else:
            return Response("Invalid Neighborhood")
    else:
        users = Neighborhood.objects.all()
        serializer = NeighborhoodSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def MyNotices(request):
    notices = News.objects.all()
    serializer = NewsSerializer(notices, many=True)
    return Response(serializer.data)
    
@api_view(['PUT', 'POST','DELETE'])
def notices(self, request, pk):
    if request.method == 'PUT':
        images = list(News.objects.filter(pk=pk).values())
        if len(images) > 0:
            serializeobj=NewsSerializer(images,data=request.data)
            if serializeobj.is_valid():
                serializeobj.save()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Bad request..."}
        else:
            datos = {'message': "Notice not found..."}
        return JsonResponse(datos)

    elif request.method == 'POST':
        newNotice = NewsSerializer(data=request.data)
        if newNotice.is_valid():
            newNotice.save()
            return Response("Notice created")
        return Response(newNotice.errors)

    elif request.method == 'DELETE':
        myNotice = News.objects.filter(pk=pk).first()
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