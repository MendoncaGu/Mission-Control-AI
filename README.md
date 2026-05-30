# Mission-Control-AI



# Regras de alerta

## Temperatura
| Condição                  | Clasificação | Mensagem Retornada                             |
| --------------------------| ------------ | ---------------------------------------------- |
| menor que 18 °C           | ATENÇÃO      | Temperatura muito baixa                        |
| de 18 °C até 30 °C        | NORMAL       | Temperatura estável                            |
| maior que 30 °C até 35 °C | ATENÇÃO      | Temperatura elevada                            |
| maior que 35 °C           | CRÍTICO      | Risco de superaquecimento                      |

## Comunicação
| Condição                           | Classificação | Mensagem Retornada   |
| ---------------------------------- | ------------- | -------------------- |
| menor que 30                       | CRÍTICO       | Sem comunicação      |
| maior ou igual a 30 e menor que 60 | ATENÇÃO       | Comunicação instável |
| maior ou igual a 60                | NORMAL        | Comunicação estável  |

## Bateria
| Condição                             | Classificação | Mensagem Retornada            |
| ------------------------------------ | ------------- | ----------------------------- |
| menor que 20%                        | CRÍTICO       | Bateria em nível crítico      |
| maior ou igual a 20% e menor que 50% | ATENÇÃO       | Bateria abaixo do recomendado |
| maior ou igual a 50%                 | NORMAL        | Energia estável               |

## Oxigênio

| Condição                             | Classificação | Mensagem Retornada        |
| ------------------------------------ | ------------- | ------------------------- |
| menor que 80%                        | CRÍTICO       | Oxigênio em nível crítico |
| maior ou igual a 80% e menor que 90% | ATENÇÃO       | Oxigênio baixo            |
| maior ou igual a 90%                 | NORMAL        | Oxigênio adequado         |

## Estabilidade Operacional

| Condição                             | Classificação | Mensagem Retornada                          |
| ------------------------------------ | ------------- | ------------------------------------------- |
| menor que 40%                        | CRÍTICO       | Estabilidade operacional em níveis críticos |
| maior ou igual a 40% e menor que 70% | ATENÇÃO       | Estabilidade operacional reduzida           |
| maior ou igual a 70%                 | NORMAL        | Estabilidade operacional adequada           |

## Classificação da Missão

| Pontuação Total   | Classificação da Missão |
| ----------------- | ----------------------- |
| de 0 até 2        | MISSÃO ESTÁVEL          |
| maior que 2 até 5 | MISSÃO EM ATENÇÃO       |
| maior que 5       | MISSÃO CRÍTICA          |
