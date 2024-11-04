from django.shortcuts import get_object_or_404, render

from chat.forms import ChatmessageCreateForm
from chat.models import ChatGroup

# Create your views here.
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="stress")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()


    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, 'chat/chat_message_p.html', context)
    return render(request,'chat/chat.html',{'chat_messages':chat_messages, 'form':form})