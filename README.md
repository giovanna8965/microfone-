# Assistente de Voz

Este é um projeto de assistente de voz que pode ouvir comandos de voz do usuário, fornecer a previsão do tempo para uma cidade especificada e gerenciar lembretes.

## Funcionalidades

- **Previsão do Tempo: Obtém e informa a previsão do tempo para uma cidade especificada.
- **Gerenciamento de Lembretes: Permite definir lembretes para datas futuras e verificar lembretes para o dia atual.

## Estrutura do Projeto

- `assistant.py`: Script principal que integra os módulos de reconhecimento de fala, síntese de fala, previsão do tempo e lembretes.
- `reminders.py`: Gerencia a definição e verificação de lembretes.
- `weather.py`: Obtém a previsão do tempo utilizando a API do OpenWeatherMap.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `speech_recognition`
  - `pyttsx3`
  - `requests`
- Microfone para entrada de voz

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
