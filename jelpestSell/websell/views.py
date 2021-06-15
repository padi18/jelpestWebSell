from .forms import DemoForm
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.contrib import messages


# Create your views here.
# https://docs.djangoproject.com/en/3.2/topics/email/

def web(request):
    return render(request, 'web.html')


def contractDemo(request):
    form = DemoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "¡Gracias! Nos pondremos en contacto contigo para hacer una Demo.")
            return redirect("/")
        else:
            messages.error(request, form.errors)
    else:
        form = DemoForm()

    return render(request, 'contractDemo.html', {'form': form})
