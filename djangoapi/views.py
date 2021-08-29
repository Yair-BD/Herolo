from .models import Message
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET'])
def apiOverView(request):
    overview = {
        "api/" : "Urls overview",
        "api/list-message" : "All messages for the log-in user",
        "api/unread-message" : "All unread messages for the log-in user",
        "api/write-message" : "Writing a message , only if the sender is the log-in user.",
        "api/read-message/<str:pk>/" : "Read a single message, only if the sender or the receiver are the log-in user. ",
        "api/delete-message/<str:pk>/" : "Delete a message, only if the sender or the receiver are the log-in user."
    }
    return Response(overview)

@api_view(['GET'])
def all_messages(request):
    recieve_messages = Message.objects.filter(reciever=request.user.id)
    send_messages = Message.objects.filter(sender=request.user.id)
    serialze_reciever = MessageSerializer(recieve_messages, many=True).data
    serialze_sender = MessageSerializer(send_messages, many=True).data
    if len(serialze_reciever) == 0 :
        serialze_reciever = "You did not recieve any message"
    else:
        serialze_reciever = {"All the messages you recieved" : MessageSerializer(recieve_messages, many=True).data}

    if len(serialze_sender) == 0:
        serialze_sender = "You did not send any message"
    else:
        serialze_sender = {"All the messages you sent" : MessageSerializer(send_messages, many=True).data}
    

    content = [serialze_reciever,serialze_sender]
    return Response(content)

@api_view(['GET'])
def all_unread_message(request):
    recievr_unread_message = Message.objects.filter(readed=False, reciever=request.user.id)
    sender_unread_message = Message.objects.filter(readed=False, sender=request.user.id )
    serialze_reciever = MessageSerializer(recievr_unread_message, many=True).data
    serialze_sender = MessageSerializer(sender_unread_message, many=True).data
    if len(serialze_reciever) == 0:
        serialze_reciever = "You read all your messages"
    else:
        serialze_reciever = {"All the unread messages you recieved" : MessageSerializer(recievr_unread_message, many=True).data}

    if len(serialze_sender) == 0:
        serialze_sender = "Your friends love to read your messages"
    else:
        serialze_sender = {"All the unread messages you sent" : MessageSerializer(sender_unread_message, many=True).data}

    content = [serialze_reciever,serialze_sender]
    return Response(content)

@api_view(['POST','GET'])
def write_message(request):
    serializer = MessageSerializer(data=request.data)
    login_user = request.user.id
    if serializer.is_valid():
        if login_user != request.data["sender"]:
            return Response("You do not have access to send this message.")
        else:
            serializer.save() 
            return Response(f"{serializer.data} has been sent successfuly")
    
    return Response(f"Know where you come from and where are you going ")
   
@api_view(['GET'])
def read_message(request, pk):
    message = Message.objects.get(id=pk)
    user = request.user
    if user != message.reciever and user != message.sender:
        return Response("You do not have access to this message.")
    else:
        serializer = MessageSerializer(message, many=False)
        return Response(serializer.data)

@api_view(['DELETE','GET'])
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    user = request.user
    if user != message.reciever and user != message.sender:
        return Response("You do not have access to DELETE this message.")
    else:
        message.delete()
        return Response("It was a grate delete")