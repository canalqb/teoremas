name: Bug report
description: Create a report to help us improve
title: "[BUG] "
labels: ["bug"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Obrigado por abrir um bug! Preencha as informações abaixo para nos ajudar a entender o problema.

  - type: input
    id: bug-description
    attributes:
      label: Descreva o bug
      description: Uma descrição clara e concisa do que está errado.
      placeholder: Ex: O script Teorema_de_Bayes.py falha com erro de tipo...
    validations:
      required: true

  - type: textarea
    id: reproduction-steps
    attributes:
      label: Como reproduzir o bug
      description: Etapas para reproduzir o comportamento
      placeholder: |
        1. Vá para '...'
        2. Clique em '....'
        3. Role para '....'
        4. Veja o erro
    validations:
      required: true

  - type: input
    id: expected-behavior
    attributes:
      label: Comportamento esperado
      description: O que você esperava que acontecesse?
      placeholder: Ex: Esperava que o script rodasse sem erro e retornasse os valores esperados.
    validations:
      required: true

  - type: textarea
    id: screenshots
    attributes:
      label: Capturas de tela (se aplicável)
      description: Se possível, adicione screenshots para ajudar a explicar o problema.

  - type: input
    id: system-desktop
    attributes:
      label: Informações do sistema (Desktop)
      description: Complete as informações do seu sistema local
      placeholder: Ex: Windows 11, Chrome 117, Python 3.12

  - type: input
    id: system-mobile
    attributes:
      label: Informações do sistema (Celular)
      description: Complete se estiver usando o celular
      placeholder: Ex: iPhone 12, iOS 15.4, Safari

  - type: textarea
    id: additional-context
    attributes:
      label: Contexto adicional
      description: Algum outro detalhe importante? Logs, saída do console, etc.

