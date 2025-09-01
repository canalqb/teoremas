---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

name: Feature request
description: Sugira uma nova funcionalidade para o projeto
title: "[FEATURE] "
labels: ["enhancement"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Obrigado por sugerir uma nova funcionalidade! Por favor, preencha os campos abaixo para ajudar a equipe a entender sua ideia.

  - type: textarea
    id: problem-description
    attributes:
      label: Existe um problema relacionado?
      description: Descreva claramente o problema que essa funcionalidade resolveria.
      placeholder: Ex: Fico sempre frustrado quando quero rodar vários teoremas de uma vez e não existe uma função agregadora...
    validations:
      required: true

  - type: textarea
    id: proposed-solution
    attributes:
      label: Descreva a solução desejada
      description: Explique de forma clara o que você gostaria que acontecesse.
      placeholder: Ex: Criar uma função `run_all_teoremas()` que execute todos os scripts em sequência.

  - type: textarea
    id: alternatives
    attributes:
      label: Alternativas consideradas
      description: Já pensou em outras formas de resolver o problema? Descreva-as aqui.
      placeholder: Ex: Também pensei em criar um CLI com argparse para selecionar os teoremas...

  - type: textarea
    id: additional-context
    attributes:
      label: Contexto adicional
      description: Adicione qualquer outra informação ou screenshots que ajudem a entender sua sugestão.
