from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .forms import messageForm
from .main import get_weather, take_user_input


def home(request):
    form = messageForm()

    # Get the message to display to view.
    if request.method == "POST":
        rawText = request.POST.get('message', '')
        context = {'rawText': rawText}
        return render(request, 'home.html', {'form': form, 'context': context['rawText']})
    else:
        return render(request, 'home.html', {'form': form})
