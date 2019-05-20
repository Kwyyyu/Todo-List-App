from django.db import models

# Create your models here.
from django.utils import timezone

class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.CharField(max_length=250) # a text field 
    #complete = models.BooleanField(default=False)
    #status = models.CharField(max_length=25,default = "Incomplete") # a text field 
    category = models.CharField(max_length=10) # a varchar
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called