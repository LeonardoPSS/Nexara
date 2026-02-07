# Nexara

Nexara é um assistente inteligente focado em clareza mental, organização de objetivos e tomada de decisão estratégica. O projeto foi pensado para rodar localmente e manter uma arquitetura modular, preparada para evoluir com integrações futuras de IA.

## Visão da arquitetura (antes do código)
A arquitetura é organizada em camadas simples e desacopladas:

- **`main.py`**: camada de interface (CLI). Coleta o objetivo, dispara o fluxo e salva o plano.
- **`core/`**: lógica de negócio pura e testável (análise de intenções, geração de tarefas, priorização e planejamento).
- **`utils/`**: utilidades transversais, como persistência de arquivos.

Cada módulo do `core` tem responsabilidade única e comunicação por dados simples (dataclasses). Isso facilita testes, manutenção e a futura substituição de heurísticas por modelos de IA sem alterar a interface.

## Estrutura do projeto
```
Nexara/
├── main.py
├── core/
│   ├── intention_analyzer.py
│   ├── task_generator.py
│   ├── prioritization_engine.py
│   ├── planner.py
│   └── models.py
├── utils/
│   └── file_manager.py
└── README.md
```

## Instalação
1. Tenha Python 3.10+ instalado.
2. Clone o repositório e execute:
   ```bash
   python main.py
   ```

## Uso
1. Informe um objetivo principal.
2. O Nexara irá extrair intenções, criar subtarefas, priorizar e gerar um plano.
3. Escolha salvar o plano em TXT ou CSV.

## Próximos passos (futuras integrações)
- Substituir heurísticas por modelos de IA (ex.: APIs de LLM).
- Persistência em banco local.
- Interface gráfica ou web.
