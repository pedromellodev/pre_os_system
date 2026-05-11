from ninja import NinjaAPI, Schema
from typing import List

from django.contrib.auth.models import User
from .models import Orcamento

api = NinjaAPI()

class OrcamentoInputSchema(Schema):
    nome_cliente: str
    cpf: str
    telefone: str
    logradouro: str
    municipio_codigo: int
    os_vistoria: str
    site: int
    economias: int
    tipo_uso: str
    descricao: str
    valor: float

class OrcamentoSchema(Schema):
    id: int
    nome_cliente: str
    cpf: str
    telefone: str
    logradouro: str
    municipio_codigo: int
    os_vistoria: str
    site: int
    economias: int
    tipo_uso: str
    descricao: str
    valor: float
    criado_em: str

@api.get("/hello")
def hello(request):
    return {"message": "Sistema PRE-OS online"}

@api.get("/orcamentos", response=List[OrcamentoSchema])
def listar_orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return orcamentos

@api.post("/orcamentos")
def criar_orcamento(request, payload: OrcamentoInputSchema):
    orcamento = Orcamento.objects.create(nome_cliente=payload.nome_cliente, cpf=payload.cpf, telefone=payload.telefone, logradouro=payload.logradouro, municipio_codigo=payload.municipio_codigo, os_vistoria=payload.os_vistoria,site=payload.site, economias=payload.economias, tipo_uso=payload.tipo_uso, descricao=payload.descricao, valor=payload.valor, criado_por=User.objects.first())
    return {"id": orcamento.id, "message": "Orçamento criado com sucesso"}