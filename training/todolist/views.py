from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import TodoList

def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["thetitle"] #title
            date = str(request.POST["date"]) #date
            content = request.POST["description"]  #content
            #complete = request.POST.get('taskComplete', False) 
            category = request.POST["category_select"] #category 
            Todo = TodoList(title=title, content=content, category=category, due_date=date)
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist("checkedbox") #checked todos to be deleted
            for todo_id in checkedlist:
                todo_id = int(todo_id)
                todo = TodoList.objects.get(id = todo_id)
                #getting todo id
            todo.delete() #deleting todo
            return redirect("/") #reloading the page
    return render(request, "index.html", {"todos": todos})