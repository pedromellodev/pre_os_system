from ninja import NinjaAPI, Schema
from typing import List

from django.contrib.auth.models import User
from .models import Orcamento
from datetime import datetime

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

class StatusUpdateSchema(Schema):
    status: str

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
    criado_em: datetime

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

@api.get("/orcamentos/{orcamento_id}", response=OrcamentoSchema)
def obter_orcamento(request, orcamento_id: int):
    orcamento = Orcamento.objects.get(id=orcamento_id)
    return orcamento

@api.patch("/orcamentos/{orcamento_id}")
def atualizar_status(request, orcamento_id: int, payload: StatusUpdateSchema):
    orcamento = Orcamento.objects.get(id=orcamento_id)
    orcamento.status = payload.status
    orcamento.save()
    return {"message": "Status atualizado com sucesso", "novo_status": orcamento.status}