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

@api_view(['GET'])
def getNote(request, primaryKey):
    note = Note.objects.get(id=primaryKey)
    serialzier = NoteSerializer(note, many=False)
    return(Response(serialzier.data))

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body'])
    serializer = NoteSerializer(note,many=False)
    return (Response(serializer.data))

@api_view(['PUT'])
def updateNote(request,primaryKey):

    note = Note.objects.get(id=primaryKey)
    serializer = NoteSerializer(note,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return (Response(serializer.data))

@api_view(['DELETE'])
def deleteNote(request,primaryKey):
    # data = request.data
    note = Note.objects.get(id=primaryKey)
    note.delete()
    return(Response("NOTE was deleted!!!!"))

@api_view(['GET'])
def getNotesList(request,start,end):
    notes = Note.objects.all()
    print(notes)
    notes = notes[int(start)-1:int(end)]
    serializer = NoteSerializer(notes,many=True)
    return(Response(serializer.data))