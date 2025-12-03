print(" Chat de Apoio e Escuta")
print("Digite 'sair' para encerrar.\n")

while True:
    mensagem = input("Você: ").lower()

    if mensagem == "sair":
        print("Chatbot: Fico feliz que tenha conversado comigo. Cuide de você. ")
        break

    # Respostas de apoio baseadas em palavras-chave simples
    if "triste" in mensagem or "mal" in mensagem or "angustiado" in mensagem:
        print("Chatbot: Sinto muito que você esteja se sentindo assim. "
              "Falar sobre isso pode ajudar um pouco. Estou aqui ouvindo. \n")

    elif "sofri" in mensagem or "bullying" in mensagem or "agressão" in mensagem:
        print("Chatbot: Lamento muito que você tenha passado por isso. "
              "Ninguém merece ser tratado dessa forma. Você não está sozinho.\n")

    elif "medo" in mensagem or "ansioso" in mensagem or "ansiedade" in mensagem:
        print("Chatbot: É compreensível sentir medo ou ansiedade às vezes. "
              "Respire fundo. Você está fazendo o melhor que pode. \n")

    elif "ajuda" in mensagem or "não sei o que fazer" in mensagem:
        print("Chatbot: Pedir ajuda já é um passo muito importante. "
              "Se puder, converse com alguém de confiança ou um profissional. "
              "Você merece apoio. \n")

    else:
        print("Chatbot: Obrigado por compartilhar isso comigo. "
              "Se quiser conversar mais, estou aqui para ouvir. \n")
