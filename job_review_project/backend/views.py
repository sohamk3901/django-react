from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CandidateSerializer
from .models import Candidate
# Create your views here.

@api_view(['GET'])
def backendOverview(request):
    api_urlS = {
        'List': '/candidate-list/',
        'Detail View': '/candidate-detail/<str:pk>/',
        'Create': '/candidate-create/',
        'Update': '/candidate-update/<str:pk>/',
        'Delete': '/candidate-delete/<str:pk>/',
    }
    return Response(api_urlS)

@api_view(['GET'])
def CandidateList(request):
    candidate = Candidate.objects.all()
    serializer = CandidateSerializer(candidate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CandidateDetail(request, pk):
    candidate = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(candidate, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CandidateCreate(request):
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def CandidateUpdate(request, pk):
    candidate = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(instance=candidate, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def CandidateDelete(request, pk):
    candidate = Candidate.objects.get(id=pk)
    candidate.delete()
    return Response("Item deleted.")
