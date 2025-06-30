from django.contrib import admin
from .models import Cursos




class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre_curso', 'carrera','turno', 'lleno', 'num_semanas',)
    search_fields = ('nombre_curso', 'carrera','turno', 'lleno', 'num_semanas',)
    date_hierarchy = 'created'
    list_filter = ('lleno','carrera')

admin.site.register(Cursos, AdministrarModelo)
