from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre_curso = models.TextField()
    carrera = models.TextField()
    turno= models.CharField(max_length=10)
    lleno = models.BooleanField(default=False)
    max_alumnos = models.SmallIntegerField(default=0)
    num_semanas = models.IntegerField(default=0)
    imagen = models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    def __str__(self):
        return self.nombre_curso