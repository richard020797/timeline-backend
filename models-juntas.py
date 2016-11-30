# models-juntas.py
class Event(models.Model):

    id_junta = models.AutoField(primary_key = True)
    horario_inicio = models.CharField(max_length = 50, default="")
    horario_fin = models.CharField(max_length = 50, default="")
    host = models.CharField(max_length = 50, default="")
    descripcion = models.TextField(default="")