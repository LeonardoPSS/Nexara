# Nexara

Nexara é um aplicativo local em Python que atua como assistente de clareza mental, organização de objetivos e tomada de decisão estratégica.

## Arquitetura
A aplicação segue arquitetura modular para facilitar evolução e integração futura com APIs de IA:

- **`main.py`**: aplicativo CLI (menu, fluxo de interação e orquestração de sessão).
- **`core/`**: regras de negócio (análise de intenções, geração de tarefas, priorização e planejamento).
- **`utils/`**: utilitários de persistência e formatação de saída.

## Estrutura
```text
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
1. Garanta Python 3.10+.
2. Execute localmente:
   ```bash
   python main.py
   ```

## Como usar
1. Abra o aplicativo e selecione **Criar novo plano estratégico**.
2. Responda às 3 perguntas da Nexara (situação, bloqueios e intenção).
3. Veja o plano priorizado na tela.
4. Consulte os arquivos gerados automaticamente em `outputs/` (TXT e CSV com timestamp).

## Evoluções sugeridas
- Conectar a análise de intenções a um modelo de linguagem (LLM).
- Adicionar histórico persistente de sessões.
- Expor API HTTP para integração com front-end.
