from django.db import models

# Create your models here.

# modelimizi oluşturduk.
class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"


# modelimizi oluşturduk.
class Student(models.Model):
    # path modelimizi ile student modelimizi ilişkilendirdik.
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    #related_name ='studensts' şeklinde bir fields olduğunu belirtmiş oluruz.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{(self.first_name).lower()} {self.last_name} " 



