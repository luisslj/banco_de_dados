# 🏦 Sistema Bancário — Banco de Dados Relacional

Este projeto define e implementa um banco de dados relacional para um sistema bancário. Ele inclui tabelas para clientes, contas, agências, funcionários, transações, cartões de crédito, empréstimos e investimentos.

---

## 📁 Estrutura do Banco de Dados

O banco é composto pelas seguintes tabelas:

- `Cliente`: informações dos clientes
- `Agencia`: dados das agências bancárias
- `Funcionario`: funcionários vinculados às agências
- `Conta`: contas bancárias dos clientes
- `Transacao`: movimentações financeiras
- `CartaoCredito`: cartões vinculados às contas
- `Emprestimo`: empréstimos contratados
- `Investimento`: aplicações financeiras

---

## 🛠️ Requisitos

- MySQL 5.7 ou superior
- Cliente MySQL (Workbench, DBeaver, CLI etc.)
- Permissões para criar banco e tabelas

---

## 🚀 Como Usar

### 1. Criar o Banco de Dados

```sql
CREATE DATABASE banco_digital;
USE banco_digital;