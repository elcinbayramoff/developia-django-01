from django.db import models

# Create your models here.
"""
ORM - Object Relation Mapping

databaza server   <--   backend
SQL query -> SELECT * FROM tasks;  X

1 databaza -> bir neçə table-lar
"""

"""
Datatiplər

CharField = Stringleri
TextField = Stringleri ( Daha böyük datalar üçün)
IntegerField = Ededleri saxlamaq
BooleanField = True, False
DateField = 15.12.2023 #2023-12-15
DateTimeField = 15.12.2023 15:12:45
EmailField = 
URLField = 
ImageField = (Pillow)
FileField = Fayllarin saxlanmasi
"""
"""
Parametrler

max_length
null
blank
default='This is description'
choices = 
unique
"""
"""
OneToOne -> User
OneToMany -> ForeignKey
ManyToMany ->

"""

"""
on_delete types

CASCADE -> Category silinse Task da silinecek
PROTECT -> Category ile bagli Task varsa, sile bilmezsen
SET_NULL -> Category silinerse, uygun field None olur
SET_DEFAULT -> Category silinerse, default deyeri alir
SET() -> Custom 
DO_NOTHING -> Category silinerse, xeta bas verir
"""

class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15,choices=[
        ('pending','Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
        ]
        , default='Pending')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deadline = models.DateField()
    
    def __str__(self):
        return f'{self.title}-{self.status}-{self.category}'

"""
CRUD

Create
Read
Update
Delete
"""

"""
Create
Task.objects.create(title="Zibili at",status="pending",category=category_instance, deadline='2025-01-20')

Read
category_instance = Category.objects.get(id=3)
"""
