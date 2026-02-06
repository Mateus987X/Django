from django.db import models
from stdimage.models import StdImageField
import uuid

def get_path_file(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateTimeField("Criação", auto_now_add=True)
    modificado = models.DateTimeField("Atualização", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = [
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Gráfico"),
        ("lni-users", "Usuários"),
        ("lni-layers", "Design"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Foguete"),
    ]
    servico = models.CharField("Serviço", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Ícone", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.servico
    
class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    name = models.CharField("Nome", max_length=100)
    cargo = models.ForeignKey("core.Cargo", verbose_name="Cargo", on_delete=models.CASCADE)
    bio = models.TextField("Bio", max_length=200)
    imagem = StdImageField("Imagem", upload_to=get_path_file, variations={"thumb": {"width": 480, "height": 480, "crop": True}})
    facebook = models.CharField("Facebook", max_length=100, default="#")
    twitter = models.CharField("Twitter", max_length=100, default="#")
    instagram = models.CharField("Instagram", max_length=100, default="#")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.name
    
class Features(Base):
    ICONE_CHOICES = [
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Gráfico"),
        ("lni-leaf", "Folha"),
        ("lni-layers", "Design"),
        ("lni-laptop-phone", "Computador e Celular"),
        ("lni-rocket", "Foguete"),
    ]
    feature = models.CharField("Feature", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Ícone", max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.feature