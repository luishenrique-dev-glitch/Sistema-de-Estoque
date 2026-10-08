# Sistema de Estoque

Sistema de gerenciamento de estoque desenvolvido em Python, com integração ao PostgreSQL.

## Sobre o projeto

Este projeto foi desenvolvido durante meus estudos em Engenharia de Software com o objetivo de praticar programação em Python, SQL e integração com banco de dados.

O sistema funciona através de um menu no terminal e permite realizar o gerenciamento de produtos.

## Funcionalidades

- Cadastro de produtos
- Listagem de produtos
- Busca de produtos
- Atualização de preço e quantidade
- Exclusão de produtos
- Ordenação por produto, preço ou quantidade
- Ordenação crescente e decrescente
- Relatório de estoque
- Cálculo da quantidade total em estoque
- Cálculo do valor total do estoque
- Identificação do produto de maior preço
- Identificação do produto de menor preço
- Identificação do produto com menor quantidade em estoque

## Tecnologias

- Python
- PostgreSQL
- SQL
- Psycopg
- python-dotenv
- Git
- GitHub

## Banco de dados

O sistema utiliza o PostgreSQL para armazenar os produtos.

Cada produto possui:

- ID
- Nome
- Preço
- Quantidade

A aplicação realiza operações de cadastro, consulta, atualização e exclusão utilizando comandos SQL através do Psycopg.

## Segurança

As informações de conexão com o banco de dados são armazenadas em variáveis de ambiente através de um arquivo `.env`.

O arquivo `.env` não deve ser enviado para o GitHub.

## Objetivo

Este projeto tem como objetivo colocar em prática conhecimentos de:

- Python
- Lógica de programação
- SQL
- CRUD
- Banco de dados relacional
- Integração entre Python e PostgreSQL
- Git e GitHub

## Próximos passos

O projeto continuará sendo aprimorado conforme avanço nos estudos de desenvolvimento de software.

## Autor

Luis Henrique Silva

Estudante de Engenharia de Software / 2º Periodo
