# NannoKit Composer

**Gerador oficial de projetos para extensões e módulos do SuperNanno**

Ferramenta de linha de comando para criar a estrutura completa de extensões `NannoKit` com um único comando.

---

## ✨ Funcionalidades

- Criação rápida de extensões completas (`nannokit-{name}`)
- Estrutura padronizada pronta para publicação no PyPI
- Templates atualizados com melhores práticas do ecossistema SuperNanno
- Suporte a variáveis (`{name}`) substituídas automaticamente
- Fácil integração com Textual + SuperNanno

---

## 📦 Instalação

### 1. Clone ou baixe o projeto

```bash
cd ~/Desktop/Bisneto/Python
git clone https://github.com/hbisneto/NannoKitComposer.git   # se estiver no GitHub
cd NannoKitComposer
```

# Directory Tree

```
NannoKitComposer
│
├── nannokit_composer
│   ├── __init__.py
│   ├── cli.py              # comandos terminal
│   ├── composer.py         # lógica principal
│   ├── templates.py        # estruturas dos projetos
│   └── generators
│       ├── __init__.py
│       ├── extension.py
│       └── module.py
│
├── setup.py
└── pyproject.toml
```