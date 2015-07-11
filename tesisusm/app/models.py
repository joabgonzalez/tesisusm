from django.db import models

# Create your models here.

class Rol_Usuario(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nb_rol = models.CharField(max_length=50)
    desc_rol = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.nb_rol,)
    
class Pregunta_Usuario(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    nb_pregunta = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.nb_pregunta,)
       
class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol_Usuario, null=True, blank=True, default=None)
    user = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)
    nb_usuario = models.CharField(max_length=50)
    ap_usuario = models.CharField(max_length=50)
    mail = models.EmailField()
    id_pregunta = models.ForeignKey(Pregunta_Usuario)
    nb_respuesta = models.CharField(max_length=50)
    fe_create =  models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s %s - (%s)" % (self.nb_usuario, self.ap_usuario, self.user)