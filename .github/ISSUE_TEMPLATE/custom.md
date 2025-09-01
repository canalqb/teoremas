name: Outro tipo de issue
description: Use este modelo para relatar dúvidas, sugestões ou qualquer outro tópico não coberto por outros templates.
title: "[DISCUSSÃO] "
labels: ["question"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Obrigado por abrir uma nova issue! Por favor, descreva abaixo o que você deseja discutir ou sugerir.

  - type: textarea
    id: general-description
    attributes:
      label: Descrição
      description: Explique de forma clara o que você gostaria de relatar, sugerir ou perguntar.
      placeholder: Ex: Tenho uma ideia para aplicar o Teorema de Bayes ao puzzle...
    validations:
      required: true

  - type: textarea
    id: context
    attributes:
      label: Contexto adicional
      description: Inclua qualquer informação extra, links, imagens ou arquivos que possam ajudar na discussão.
      placeholder: Ex: Encontrei um artigo que pode ajudar na formulação matemática...
