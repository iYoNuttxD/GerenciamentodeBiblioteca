# Gerenciador de Biblioteca

O **Gerenciador de Biblioteca** é uma aplicação desenvolvida em Python para facilitar a administração de empréstimos, cadastros de livros e controle de alunos em um sistema de biblioteca. O sistema oferece funcionalidades para gerenciar acervos, verificar disponibilidade de livros e realizar o controle de usuários cadastrados.

## Visão Geral

O objetivo deste projeto é proporcionar uma solução simples e eficiente para o gerenciamento de bibliotecas, com foco em:

- Cadastro e gerenciamento de livros.
- Controle de alunos e seus empréstimos.
- Verificação de disponibilidade de exemplares.
- Manutenção do acervo.

## Funcionalidades Principais

1. **Cadastro e Gerenciamento de Alunos**
   O sistema permite o cadastro de alunos com seus dados pessoais, além de gerenciar o histórico de empréstimos e devoluções.

2. **Cadastro e Gerenciamento de Livros**
   Os livros são cadastrados com seus detalhes, incluindo título, autor, número de exemplares e status de disponibilidade. É possível adicionar, editar ou remover livros do sistema.

3. **Empréstimos e Devoluções**
   O sistema controla os empréstimos de livros, permitindo aos alunos retirar exemplares e registrando as datas de devolução.

4. **Verificadores e Utilidades**
   O projeto inclui diversas ferramentas utilitárias e verificadores para garantir que as operações no sistema sejam feitas corretamente, como a validação de entradas e a gestão eficiente do acervo.

## Requisitos de Instalação

1. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/seuusuario/gerenciador-biblioteca.git
   ```

2. Certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido utilizando Python 3.x.

3. Instale as bibliotecas necessárias utilizando o comando:
   ```bash
   pip install pickle5 re
   ```

4. Execute o sistema.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento de todo o sistema.
- **Pickle**: Utilizado para persistir dados de livros em arquivo.
- - -**re**: Utilizado para realizar operações de expressões regulares.
