
import unicodedata


def normalizar(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize('NFD', texto)

    texto = ''.join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != 'Mn'
    )

    return texto


def responder(mensagem):
    mensagem = normalizar(mensagem)

    # Saudacoes
    if any(palavra in mensagem for palavra in [
        "oi", "ola", "bom dia", "boa tarde", "boa noite"
    ]):
        return (
            "Ola! Seja bem-vindo a nossa loja de frango assado! "
            "Como posso ajudar voce hoje?"
        )

    # Cardapio completo
    elif any(palavra in mensagem for palavra in [
        "cardapio", "menu", "lista de produtos",
        "quais produtos", "o que voces vendem"
    ]):
        return (
            "Confira nosso cardapio:\n\n"
            "Frango assado inteiro: R$ 35,00\n"
            "Batata: R$ 8,00\n"
            "Farofa: R$ 5,00\n"
            "Coca-Cola 350 ml: R$ 5,00"
        )

    # Precos
    elif any(palavra in mensagem for palavra in [
        "preco", "precos", "quanto custa", "valor"
    ]):
        return (
            "Nossos precos sao:\n"
            "Frango assado inteiro: R$ 35,00\n"
            "Batata: R$ 8,00\n"
            "Farofa: R$ 5,00\n"
            "Coca-Cola 350 ml: R$ 5,00"
        )

    # Frango
    elif "frango" in mensagem:
        return (
            "Temos frango assado inteiro por R$ 35,00! "
            "Gostaria de fazer um pedido?"
        )

    # Batata
    elif "batata" in mensagem:
        return "Temos batata por R$ 8,00. Gostaria de adicionar ao pedido?"

    # Farofa
    elif "farofa" in mensagem:
        return "Temos farofa por R$ 5,00. Gostaria de adicionar ao pedido?"

    # Refrigerante
    elif any(palavra in mensagem for palavra in [
        "coca", "refrigerante", "bebida"
    ]):
        return "Temos Coca-Cola de 350 ml por R$ 5,00."

    # Entrega
    elif any(palavra in mensagem for palavra in [
        "entrega", "entregar", "delivery", "endereco"
    ]):
        return (
            "Posso ajudar com seu pedido! Para confirmar "
            "as condicoes de entrega, fale com nosso atendente."
        )

    # Atendente
    elif any(palavra in mensagem for palavra in [
        "atendente", "humano", "pessoa", "falar com alguem"
    ]):
        return (
            "Claro! Nossa equipe pode ajudar voce. "
            "Entre em contato com um atendente."
        )

    # Agradecimento
    elif any(palavra in mensagem for palavra in [
        "obrigado", "obrigada", "valeu"
    ]):
        return "Nos agradecemos! Sera um prazer atender voce!"

    # Despedida
    elif any(palavra in mensagem for palavra in [
        "tchau", "ate logo", "ate mais"
    ]):
        return "Obrigado pela preferencia! Volte sempre!"

    # Resposta padrao
    else:
        return (
            "Desculpe, ainda nao consegui entender sua pergunta. "
            "Voce pode perguntar sobre nosso cardapio, produtos, "
            "precos ou falar com um atendente."
        )
import unicodedata


def normalizar(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize('NFD', texto)

    texto = ''.join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != 'Mn'
    )

    return texto


def responder(mensagem):
    mensagem = normalizar(mensagem)

    # Saudacoes
    if any(palavra in mensagem for palavra in [
        "oi", "ola", "bom dia", "boa tarde", "boa noite"
    ]):
        return (
            "Ola! Seja bem-vindo a nossa loja de frango assado! "
            "Como posso ajudar voce hoje?"
        )

    # Cardapio completo
    elif any(palavra in mensagem for palavra in [
        "cardapio", "menu", "lista de produtos",
        "quais produtos", "o que voces vendem"
    ]):
        return (
            "Confira nosso cardapio:\n\n"
            "Frango assado inteiro: R$ 35,00\n"
            "Batata: R$ 8,00\n"
            "Farofa: R$ 5,00\n"
            "Coca-Cola 350 ml: R$ 5,00"
        )

    # Precos
    elif any(palavra in mensagem for palavra in [
        "preco", "precos", "quanto custa", "valor"
    ]):
        return (
            "Nossos precos sao:\n"
            "Frango assado inteiro: R$ 35,00\n"
            "Batata: R$ 8,00\n"
            "Farofa: R$ 5,00\n"
            "Coca-Cola 350 ml: R$ 5,00"
        )

    # Frango
    elif "frango" in mensagem:
        return (
            "Temos frango assado inteiro por R$ 35,00! "
            "Gostaria de fazer um pedido?"
        )

    # Batata
    elif "batata" in mensagem:
        return "Temos batata por R$ 8,00. Gostaria de adicionar ao pedido?"

    # Farofa
    elif "farofa" in mensagem:
        return "Temos farofa por R$ 5,00. Gostaria de adicionar ao pedido?"

    # Refrigerante
    elif any(palavra in mensagem for palavra in [
        "coca", "refrigerante", "bebida"
    ]):
        return "Temos Coca-Cola de 350 ml por R$ 5,00."

    # Entrega
    elif any(palavra in mensagem for palavra in [
        "entrega", "entregar", "delivery", "endereco"
    ]):
        return (
            "Posso ajudar com seu pedido! Para confirmar "
            "as condicoes de entrega, fale com nosso atendente."
        )

    # Atendente
    elif any(palavra in mensagem for palavra in [
        "atendente", "humano", "pessoa", "falar com alguem"
    ]):
        return (
            "Claro! Nossa equipe pode ajudar voce. "
            "Entre em contato com um atendente."
        )

    # Agradecimento
    elif any(palavra in mensagem for palavra in [
        "obrigado", "obrigada", "valeu"
    ]):
        return "Nos agradecemos! Sera um prazer atender voce!"

    # Despedida
    elif any(palavra in mensagem for palavra in [
        "tchau", "ate logo", "ate mais"
    ]):
        return "Obrigado pela preferencia! Volte sempre!"

    # Resposta padrao
    else:
        return (
            "Desculpe, ainda nao consegui entender sua pergunta. "
            "Voce pode perguntar sobre nosso cardapio, produtos, "
            "precos ou falar com um atendente."
        )
