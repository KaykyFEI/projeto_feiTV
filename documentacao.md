# Documentação do projeto feiTV #

## **Lógica do Cadastro** ##

O programa é executado. Aparecem as opções:

- Criar conta

- Fazer login

- Buscar vídeo

- Gerenciar favoritos

- Lista de Reprodução

- Fazer login como admin

- Sair

### **Passo 1:** ###

O usuário seleciona a opção criar conta. O programa irá solicitar um e-mail para cadastro e dá opções de voltar e outra de sair. O programa checa se o e-mail fornecido já existe no arquivo com os dados persistentes. Se existir, o programa retorna uma mensagem de erro e solicita novamente um e-mail. Se não existir, o programa segue para o próximo passo.

### **Passo 2:** ###

O programa solicita um nome de usuário e dá opções de voltar e outra de sair. Ele verifica se o nome de usuário fornecido já existe no arquivo. Se sim, mostra mensagem de erro e solicita novamente. Se não, ele para o próximo passo.

### **Passo 3:** ###

O programa solicita uma senha informando os requisitos e dá opções de voltar e outra de sair. Os requisitos são:

- Ter no mínimo 8 caracteres e no máximo 16 caracteres

- Ter número

- Ter letras, sendo pelo menos uma maiúscula e uma minúscula

- Ter símbolos

Se a senha fornecida não atender esses requisitos, o programa retorna um erro, informando o que não foi atendido. Se a senha atender os requisitos, segue para o próximo passo.

### **Passo 4:** ###

O programa solicita uma dica. Ele informa que a dica deve ser uma palavra de até **50 caracteres**. O programa verifica o tamanho da palavra. Se for maior que 50, retorna erro, informando ele, e pede para inserir novamente. Se não for maior, ele reexibe a dica e dá duas opções ao usuário: "Confirmar" e "Alterar". Se o usuário selecionar "Alterar", o programa solicita novamente a dica e faz as verificações. Se ele selecionar "Confirmar", o programa segue para o próximo passo.

### **Passo 5:** ###

O programa informa que o cadastro foi realizado com sucesso. Aparece a opção ao usuário de voltar ao menu inicial ou sair do programa.
