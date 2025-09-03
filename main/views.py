from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406358472',
        'name': 'Tristan Rasheed Satria',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
