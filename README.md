# Sistema IoT para Monitoramento de Vento e Controle de Hélices - Usina Eólica

Este é um sistema IoT desenvolvido para monitoramento da velocidade do vento e controle automático das hélices de uma usina eólica. O objetivo principal é otimizar a produção de energia e garantir a segurança da usina, ajustando a velocidade das hélices com base na velocidade do vento medida em tempo real.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para implementar a lógica do sistema.
- **Paho MQTT**: Biblioteca utilizada para comunicação entre os dispositivos IoT via protocolo MQTT.
- **Broker MQTT (Mosquitto)**: Broker público de MQTT utilizado para comunicação dos dados entre os dispositivos.
- **Node Red**: Ferramenta gráfica utilizada para explorar e monitorar tópicos MQTT, facilitando o teste e visualização das mensagens publicadas.

## Funcionalidade

O sistema coleta dados sobre a velocidade do vento a partir de um sensor (anemômetro) e, com base nesses dados, ajusta a velocidade das hélices da usina eólica. Quando a velocidade do vento ultrapassa 10 m/s, o sistema diminui automaticamente a velocidade das hélices para garantir a segurança da usina.

### Fluxo do Sistema:

1. **Conexão com o Broker MQTT**: O cliente MQTT se conecta ao broker público `test.mosquitto.org` na porta padrão `1883`.
2. **Coleta de Dados de Vento**: O sistema gera valores aleatórios de velocidade do vento entre 1 e 150 km/s(No caso está de 1 a 15 para simplificar o entendimento no código) representando a entrada de dados do anemômetro.
3. **Publicação de Dados**: O valor da velocidade do vento é publicado em um tópico MQTT específico: `srs/inatel/sec/c115/vento/eolica`.
4. **Controle de Hélices**: Com base no valor do vento:
    - Se o vento for maior ou igual a 100 km/s (No caso está 10 no código para simplificar o entendimento), o sistema simula a redução da velocidade das hélices.
    - Caso contrário, o sistema informa que tudo está funcionando normalmente.
5. **Execução Contínua**: O sistema continua executando, coletando e publicando dados a cada 5 segundos.

## Requisitos

Antes de executar o código, você precisa garantir que tenha o Python instalado em sua máquina. Além disso, é necessário instalar a biblioteca `paho-mqtt`:

```bash
pip install paho-mqtt
