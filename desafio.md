```markdown
# Desafio: Criar View para Adicionar um Post no Blog

## 🎯 Objetivo
Implementar uma **nova funcionalidade no blog** que permita **adicionar um novo post**, utilizando uma view própria e um formulário, integrando com a estrutura já existente do projeto.

> 💡 **Importante:**  
> Você **já possui**:
> - A estrutura do blog criada  
> - O model de Post  
> - A view e o template que **listam os posts do blog**

Nesta tarefa, você irá **apenas adicionar a funcionalidade de criação de posts**.

---

## 📌 Passo a passo do que deve ser feito

### 1. Criar a nova view
- Crie uma view responsável por **exibir o formulário** e **processar o envio dos dados** do novo post.
- Essa view deve tratar:
  - A exibição do formulário quando a página é acessada
  - O salvamento do post quando o formulário é enviado

---

### 2. Criar o template do formulário
- Crie um novo template HTML para a página de **criação de post**
- Esse template deve conter:
  - Um formulário
  - Campos correspondentes aos dados do post (título, conteúdo, etc.)
  - Um botão para enviar o formulário

---

### 3. Configurar a rota (URL)
- Crie uma nova rota que:
  - Aponte para a view de criação de post
  - Tenha um caminho claro, como algo relacionado a “novo post” ou “criar post”

---

### 4. Conectar o formulário à view
- Garanta que o formulário:
  - Envie os dados corretamente para a view

---

### 5. Salvar o post no banco de dados
- Ao receber os dados do formulário:
  - Crie um novo objeto de post
  - Salve esse post no banco de dados

---

### 6. Redirecionar após a criação
- Após o post ser salvo com sucesso:
  - Redirecione o usuário para a página que **lista os posts do blog**
  - Assim, o novo post deve aparecer automaticamente na listagem

---

### 7. Testar a funcionalidade
- Acesse a página de criação de post
- Preencha o formulário
- Envie os dados
- Verifique se:
  - O post foi criado corretamente
  - Ele aparece na página de listagem do blog

---

## ✅ Resultado esperado
Ao final da tarefa, o blog deve permitir:
- Acessar uma página para criar novos posts
- Visualizar o novo post na lista existente do blog

## 📌 Entrega do Desafio

Você pode entregar este desafio seguindo as instruções abaixo:

- Publique o seu projeto em um **repositório no GitHub** (sua conta pessoal)
- Certifique-se de que o código esteja funcionando corretamente
- Acesse o **repositório do projeto original** (este)
- Abra uma **Issue** no projeto
- No corpo da Issue, informe:
  - O **link do seu repositório no GitHub**
  - Seu **nome** (ou identificação combinada em aula)

🔍 Assim podemos dar uma olhada e quem saber retornar um feedback!

Boa prática! 🚀

---
```
