from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single note object'
        },
        {
            'Endpoint':'/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Create new note with datat sent in post req'
        },
        {
            'Endpoint':'/notes/id/update/',
            'method':'PUT',
            'body':{'body':''},
            'description':'Creste an existing note with data sent in'
        },
        {
            'Endpoint':'/notes/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing note'
        },
        
    ]
    
    return(Response(routes))

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    #cant directly return notes as they are objects not json data
    serializer = NoteSerializer(notes,many = True)
    return(Response(serializer.data))