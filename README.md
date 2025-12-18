# TikTok TTS Handler

Projeto em Python que conecta a uma live do TikTok, captura comentários em tempo real e os reproduz via Text-to-Speech (TTS), com sistema de fila de áudio, validação de texto e atalhos de controle.

---

## Funcionalidades

* Conexão automática a lives do TikTok
* Leitura de comentários em tempo real
* Conversão de texto para áudio (TTS)
* Fila de reprodução de áudio
* Filtro de palavras proibidas (blacklist)
* Tratamento de caracteres UTF-8 / ASCII
* Atalho de teclado para pular o áudio atual
* Configuração totalmente baseada em JSON

---

## Estrutura do Projeto

```
├── TikTokHandler.py      # Núcleo do projeto (listener + player)
├── TTSHandler.py         # Conversão de texto em áudio (TTS)
├── TextValidation.py     # Validação e filtragem de texto
├── config.json           # Arquivo de configuração
└── utils/
    └── debug.py          # Utilitário de debug (opcional)
```

---

## Requisitos

* Python 3.9+

### Dependências

Instale todas com:

```bash
pip install TikTokLive gTTS pydub pygame keyboard
```

> **Observação:** O `pydub` pode exigir o **FFmpeg** instalado e configurado no PATH do sistema.

---

## Configuração (`config.json`)

```json
{
  "username": "nome_do_tiktok",
  "command": "",
  "skipShortCut": "q",
  "language": "pt-br",
  "debug": true,
  "blacklist-words": ["palavra1", "palavra2"],
  "ascii-only": true,
  "dont-say-message-if-contains-utf-8": false
}
```

### Campos

* **username**: Nome do usuário do TikTok (live alvo)
* **command**: Prefixo obrigatório do comentário (ex: `!tts`). Vazio = todos
* **skipShortCut**: Tecla para interromper o áudio atual
* **language**: Idioma do TTS (ex: `pt-br`, `en`)
* **blacklist-words**: Palavras que impedem a leitura
* **ascii-only**: Remove caracteres não ASCII
* **dont-say-message-if-contains-utf-8**: Ignora mensagens com UTF-8

---

## Como Executar

```bash
python TikTokHandler.py
```

Ao iniciar:

* O bot conecta na live automaticamente
* Comentários válidos entram na fila de áudio
* O áudio é reproduzido sequencialmente

---

## Validação de Texto

O módulo `TextValidation.py`:

* Bloqueia palavras da blacklist
* Remove ou ignora caracteres fora do padrão ASCII
* Retorna `False` se o comentário não for válido

---

## Atalho de Teclado

* Pressione a tecla configurada em `skipShortCut` para pular o áudio atual

---

## Observações Técnicas

* O áudio é reproduzido via `pygame.mixer`
* A fila é gerenciada com `collections.deque`
* O sistema é totalmente assíncrono (`asyncio`)

---

## Possíveis Melhorias Futuras

* Sistema de whitelist
* Cache de áudio
* Interface gráfica
* Suporte a múltiplas vozes
* Controle por comandos no chat

---

## Aviso Legal

Este projeto não é afiliado ao TikTok. Use por sua conta e risco, respeitando os termos da plataforma.

---

## Licença

Uso livre para fins educacionais e pessoais.
