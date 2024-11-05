from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render (request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  
    serializer_class = MenuSerializer 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class= BookingSerializer	
    permission_classes = [IsAuthenticated]	

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]