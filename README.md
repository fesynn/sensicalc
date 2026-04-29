# SensiCalc - by fesynn

Conversor de sensibilidade para jogos FPS.

Informe sua sensibilidade atual, o jogo de origem e o destino — o SensiCalc calcula
a sensibilidade equivalente levando em conta o multiplicador interno de cada jogo,
mudança de DPI e diferença de peso entre mouses.

---

## Funcionalidades

- Conversão de sensibilidade entre jogos (CS2, Valorant, Apex, Overwatch 2, R6 Siege, Fortnite)
- Ajuste automático para mudança de DPI
- Ajuste para troca de mouse com peso diferente
- Interface web simples, roda localmente no navegador

---

## Como funciona o cálculo

Cada jogo tem uma constante chamada **yaw** — quantos graus a tela gira por unidade
de sensibilidade. A conversão universal é:

## sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn sYnn 

sens_destino = sens_origem × (yaw_origem / yaw_destino)

Se o DPI mudar:
sens_final = sens_calculada × (dpi_antigo / dpi_novo)

Se o peso do mouse mudar:
sens_final = sens_calculada × (peso_novo / peso_antigo)

---

## Como rodar o projeto

### Pré-requisitos
- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/fesynn/sensicalc.git
cd sensicalc

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python main.py
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Testes

```bash
pytest tests/ -v
```

---

## Jogos suportados

| Jogo | Yaw |
|---|---|
| Counter-Strike 2 | 0.022 |
| Valorant | 0.07 |
| Apex Legends | 0.022 |
| Overwatch 2 | 0.0066 |
| Rainbow Six Siege | 0.00573 |
| Fortnite | 0.5590 |

---

## Tecnologias

- Python 3 + Flask
- HTML, CSS, JavaScript
- pytest

---

## Estrutura do projeto
sensicalc/
├── app/
│   ├── init.py      # Application factory
│   ├── routes.py        # Endpoints Flask
│   ├── calculator.py    # Lógica de cálculo
│   └── games.py         # Dados dos jogos
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── tests/
│   └── test_calculator.py
├── main.py
├── requirements.txt
└── README.md

## sYnn SyNN syNN Synn SyNn