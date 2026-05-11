from ninja import NinjaAPI, Schema
from typing import List

from .models import Orcamento

api = NinjaAPI()

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