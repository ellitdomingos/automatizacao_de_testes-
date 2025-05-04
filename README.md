# Automatização de Testes no Git com GitHub Actions

Este projeto demonstra como automatizar testes em um pipeline de Machine Learning diretamente no fluxo de versionamento com Git e GitHub Actions.

A cada `push` ou `pull request` para o branch `main`, os testes definidos são executados automaticamente. Isso garante a confiabilidade do código e a integração contínua (CI).

Embora o foco deste projeto seja em Machine Learning, a estrutura pode ser aplicada a outros tipos de testes, como testes de backend ou frontend, desde que os workflows sejam devidamente configurados no GitHub Actions.

## Estrutura do Projeto

ml-auto-test/
```
├── app/                  -> Código do modelo
├── tests/                -> Testes automatizados
├── .github/workflows/    -> Configuração do GitHub Actions
├── requirements.txt      -> Dependências
└── README.md             -> Documentação
````

## Descrição

Este projeto utiliza um modelo simples de regressão linear (`y = 2x`) implementado com `scikit-learn`. O objetivo é mostrar como testes automatizados com `pytest` podem ser integrados ao ciclo de desenvolvimento usando GitHub Actions.

## O que é testado?

- O coeficiente do modelo após o treinamento
- A predição correta para um valor de entrada conhecido

## Como Executar os Testes

### 1. Instalar as dependências

Navegue até o diretório do projeto e execute:

```bash
pip install -r requirements.txt
```

![image](https://github.com/user-attachments/assets/0cad7276-8e86-4b58-86d8-803fd4b36710)
