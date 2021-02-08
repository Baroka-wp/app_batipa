def index(request):
    message = "salut tout le monde !"
    return HttpResponse(message)