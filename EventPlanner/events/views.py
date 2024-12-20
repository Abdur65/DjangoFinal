from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import ListView, CreateView, FormView

from events.models import Event
from events.serializers import Event


from rest_framework import permissions
from rest_framework.response import Response

# Event views
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    
class EventCreateView(CreateView):
    model = Event
    # form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event-list')
    
class EventListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        print(request.user)
        event = Event.objects.all()
        serializer = EventSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

