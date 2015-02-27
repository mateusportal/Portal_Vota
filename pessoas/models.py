from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.CharField(default='semfoto.png', max_length=100, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=False)
    email = models.CharField(db_index=True, max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(db_index=True, max_length=14, blank=True, null=True)
    ativo = models.CharField(default='SIM', max_length=3, blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __init__(self,*args, **kwargs):
        super(Pessoa, self).__init__(*args, **kwargs)
        self.foto = 'semfoto.png'
        self.ativo = 'SIM'

    def __unicode__(self):
        return self.nome+' - '+self.email

class Voto(models.Model):
    id = models.AutoField(primary_key=True)
    remetente = models.ForeignKey(Pessoa, related_name="remetente")
    destinatario = models.ForeignKey(Pessoa, related_name="destinatario")
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return 'De:'+self.remetente.nome+' Para:'+self.destinatario.nome

