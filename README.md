# Pacoa API

API para gestão de beneficiários do [Projeto Social Pacoa](https://www.facebook.com/projetopacoa/?locale=pt_BR).

### Setup

- Clone e instalação dos pacotes necessários

```
git clone git@github.com:gabrielbdornas/pacoa-api.git
cd pacoa-api

# Linux enviroment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Windows enviroment
python -m venv venv
source venv/Script/activate
pip install -r requirements.txt
```

- Migração do bando de dados:

```
flask db init # cria pasta de migração (inicia o processo).
flask db migrate # cria a migração
flask db upgrade # inclui mudanças no banco
```

Por fim, basta executar `task server` para rodar a API localmente.

Obs.: Para realizar queries no banco de dados via terminal interativo Python rodar:

```
$ python
from app import create_app
create_app().app_context().push()
```

### Fluxo registro de presença

```mermaid
flowchart TD
  1((Recebe qualquer mensagem))-->2
  2{"`Número de celular cadastrado?`"}-->|Sim|3
  2-->|Não|4
  4[[Número de celular não cadastrado.]]-->5
  5((Fim))
  3[["`**Opções**:
  1 - Digite o início do nome do beneficiário.
  2 - Sair.`"]]-->|2|6
  6[[Para reiniciar basta enviar qualquer mensagem.]]
  6-->5
  3-->|1|11
  11["`**Nomes disponíveis:**
    - id: Nome.
    - id: Nome.
    **Opções:**
    - Digite o número do beneficiário desejado.
    2 - Retornar opção de pesquisa de nome.
    3 - Sair.
  `"]
  11-->|3|6
  11-->|2|3
  11-->|Número do beneficiário|12
  12{Número do beneficiário existente?}-->|Sim|7
  12-->|Não|13
  13[[Número beneficiário não existente]]-->3
  7[["`**Informações do Beneficiário:**
    Nome:
    Sexo:
    Data de Nascimento:
    Idade:
    Última presença registrada:
    **Opções**
    1 - Marcar presença.
    2 - Desmarcar presença.
    3 - Consultar presenças.
    4 - Sair.
  `"]]
  7-->|4|6
  7-->|1|9
  9["`**Opções**:
    1 - Marcar presença hoje.
    2 - Retornar opção de pesquisa de nome.
    3 - Sair.
  `"]
  9-->|3|6
  9-->|1|10
  10[[Presença `Nome beneficiário` marcada com sucesso.]]-->3
  9-->|2|3
```
