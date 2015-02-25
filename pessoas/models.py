from django.db import models

class Pessoa(models.Model):
    foto = models.CharField(default='semfoto.png', max_length=100, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=False)
    email = models.CharField(db_index=True, max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(db_index=True, max_length=14, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __init__(self):
        self.foto = 'semfoto.png'

    def __unicode__(self):
        return self.nome+' - '+self.email

class Voto(models.Model):
    remetente = models.ForeignKey(Pessoa, related_name="remetente")
    destinatario = models.ForeignKey(Pessoa, related_name="destinatario")
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return 'De:'+self.remetente.nome+' Para:'+self.destinatario.nome

