from django.http import HttpResponse


def health(request):
    """Health check endpoint that returns HTTP 200 OK"""
    return HttpResponse("OK", status=200)


def home(request):
    """Home page view"""
    return HttpResponse("Welcome to Django Demo!", status=200)


def todo_list(request):
    """Home page with TODO list"""
    return HttpResponse("TODO List - This will show all todos", status=200)


def todo_add(request):
    """Add new TODO"""
    return HttpResponse("Add New TODO - This will have a form to add todos", status=200)


def todo_edit(request, todo_id):
    """Edit TODO"""
    return HttpResponse(f"Edit TODO {todo_id} - This will have a form to edit todo {todo_id}", status=200)


def todo_delete(request, todo_id):
    """Delete TODO"""
    return HttpResponse(f"Delete TODO {todo_id} - This will confirm deletion of todo {todo_id}", status=200)
