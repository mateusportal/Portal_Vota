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

    '''def campeoes(self):
        #http://stackoverflow.com/questions/3543379/django-annotate-groupings-by-month
        from django.db.models import Count
        Voto.objects.all().extra(select={'year': 'extract(year from data_cadastro )'}).values('year').annotate(dcount=Count('pub_date'))

        values('actor').annotate(total=Count('actor')).order_by('total')

        #from django.db import connection, transaction
        #cursor = connection.cursor()
        #cursor.execute('select extract(year from data_cadastro) as ano, extract(month from data_cadastro) as mes, destinatario_id, count(destinatario_id) as votos FROM pessoas_voto group by ano, mes, destinatario_id order by ano desc, mes desc, votos desc')
        #dados = cursor.fetchone()
        #return dados
    '''

    def __unicode__(self):
        return 'De:'+self.remetente.nome+' Para:'+self.destinatario.nome

