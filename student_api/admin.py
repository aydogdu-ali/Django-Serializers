from django.contrib import admin



from .models import Student, Path #oluşturduğumuz modeli admin panelde görmek için import ediyoruz.
admin.site.register(Student)
admin.site.register(Path)

