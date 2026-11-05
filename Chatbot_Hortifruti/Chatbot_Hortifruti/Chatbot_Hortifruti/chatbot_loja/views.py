
from django.shortcuts import render, redirect
from chatbot_loja.models import Pedido, ItemPedido
from urllib.parse import quote


def home(request):
    return render(request, 'loja/home.html')


def produtos(request):
    lista_produtos = [
        {'id': 1, 'nome': 'Frango assado inteiro', 'preco': 35.00},
        {'id': 2, 'nome': 'Batata', 'preco': 8.00},
        {'id': 3, 'nome': 'Farofa', 'preco': 5.00},
        {'id': 4, 'nome': 'Coca-Cola 350 ml', 'preco': 5.00},
    ]

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        carrinho = request.session.get('carrinho', {})

        if produto_id:
            carrinho[produto_id] = carrinho.get(produto_id, 0) + 1
            request.session['carrinho'] = carrinho

        return redirect('produtos')

    carrinho = request.session.get('carrinho', {})
    quantidade_carrinho = sum(carrinho.values())

    return render(
        request,
        'loja/produtos.html',
        {
            'produtos': lista_produtos,
            'quantidade_carrinho': quantidade_carrinho
        }
    )



def carrinho(request):
    lista_produtos = [
        {'id': 1, 'nome': 'Frango assado inteiro', 'preco': 35.00},
        {'id': 2, 'nome': 'Batata', 'preco': 8.00},
        {'id': 3, 'nome': 'Farofa', 'preco': 5.00},
        {'id': 4, 'nome': 'Coca-Cola 350 ml', 'preco': 5.00},
    ]

    carrinho = request.session.get('carrinho', {})

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        acao = request.POST.get('acao')

        if produto_id:
            produto_id = str(produto_id)
            quantidade = carrinho.get(produto_id, 0)

            if acao == 'aumentar':
                carrinho[produto_id] = quantidade + 1

            elif acao == 'diminuir':
                if quantidade > 1:
                    carrinho[produto_id] = quantidade - 1
                else:
                    carrinho.pop(produto_id, None)

        request.session['carrinho'] = carrinho
        return redirect('carrinho')

    itens = []
    total = 0

    for produto in lista_produtos:
        quantidade = carrinho.get(str(produto['id']), 0)

        if quantidade > 0:
            subtotal = produto['preco'] * quantidade

            itens.append({
                'id': produto['id'],
                'nome': produto['nome'],
                'preco': produto['preco'],
                'quantidade': quantidade,
                'subtotal': subtotal,
            })

            total += subtotal

    return render(
        request,
        'loja/carrinho.html',
        {'itens': itens, 'total': total}
    )



def remover_produto(request, produto_id):
    if request.method == 'POST':
        carrinho = request.session.get('carrinho', {})
        produto_id = str(produto_id)

        if produto_id in carrinho:
            del carrinho[produto_id]

        request.session['carrinho'] = carrinho

    return redirect('carrinho')


import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from chatbot_loja.chatbot import responder


@ensure_csrf_cookie
def pagina_chatbot(request):
    return render(request, 'loja/chatbot.html')



@require_POST
def responder_chatbot(request):
    try:
        dados = json.loads(request.body)
        mensagem = dados.get('mensagem', '').strip()

        if not mensagem:
            return JsonResponse({
                'resposta': 'Por favor, digite uma mensagem.'
            })

        resposta = responder(mensagem)

        mensagem_busca = mensagem.lower()

        link = None
        texto_link = None

        # Falar com atendente pelo WhatsApp
        if any(palavra in mensagem_busca for palavra in [
            'atendente', 'humano', 'pessoa',
            'falar com alguem', 'falar com alguém',
            'vendedor', 'suporte'
        ]):
            link = (
                'https://wa.me/5511967929855?text=' +
                quote('Olá! Gostaria de falar com um atendente da loja.')
            )
            texto_link = 'Conversar com atendente pelo WhatsApp'

            resposta = (
                'Claro! Clique no botão abaixo para conversar '
                'diretamente com nosso atendente pelo WhatsApp.'
            )

        return JsonResponse({
            'resposta': resposta,
            'link': link,
            'texto_link': texto_link
        })

    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({
            'resposta': 'Não consegui entender a mensagem enviada.'
        })

    
def finalizar_compra(request):
    carrinho = request.session.get('carrinho', {})

    if not carrinho:
        return redirect('produtos')

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        entrega = request.POST.get('entrega', '')
        endereco = request.POST.get('endereco', '').strip()
        pagamento = request.POST.get('pagamento', '')

        if not nome or not telefone or not entrega or not pagamento:
            return render(request, 'loja/finalizar_compra.html', {
                'erro': 'Preencha todos os campos obrigatórios.'
            })

        if entrega == 'entrega' and not endereco:
            return render(request, 'loja/finalizar_compra.html', {
                'erro': 'Informe o endereço de entrega.'
            })

        request.session.pop('pedido_id', None)
        request.session['dados_pedido'] = {
            'nome': nome,
            'telefone': telefone,
            'entrega': entrega,
            'endereco': endereco,
            'pagamento': pagamento,
        }

        return redirect('confirmar_pedido')

    return render(request, 'loja/finalizar_compra.html')


def confirmar_pedido(request):
    dados_pedido = request.session.get('dados_pedido')

    if not dados_pedido:
        return redirect('carrinho')

    lista_produtos = [
        {'id': 1, 'nome': 'Frango assado inteiro', 'preco': 35.00},
        {'id': 2, 'nome': 'Batata', 'preco': 8.00},
        {'id': 3, 'nome': 'Farofa', 'preco': 5.00},
        {'id': 4, 'nome': 'Coca-Cola 350 ml', 'preco': 5.00},
    ]

    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0

    for produto in lista_produtos:
        quantidade = carrinho.get(str(produto['id']), 0)

        if quantidade > 0:
            subtotal = produto['preco'] * quantidade

            itens.append({
                'nome': produto['nome'],
                'quantidade': quantidade,
                'subtotal': subtotal,
            })

            total += subtotal

    # Verificar se o pedido já foi salvo
    pedido_id = request.session.get('pedido_id')

    if pedido_id:
        pedido = Pedido.objects.get(id=pedido_id)
    else:
        pedido = Pedido.objects.create(
            nome=dados_pedido['nome'],
            telefone=dados_pedido['telefone'],
            entrega=dados_pedido['entrega'],
            endereco=dados_pedido['endereco'],
            pagamento=dados_pedido['pagamento'],
            total=total
        )

        for item in itens:
            ItemPedido.objects.create(
                pedido=pedido,
                produto=item['nome'],
                quantidade=item['quantidade'],
                preco=next(
                    p['preco'] for p in lista_produtos
                    if p['nome'] == item['nome']
                )
            )

        request.session['pedido_id'] = pedido.id

    return render(request, 'loja/confirmar_pedido.html', {
        'dados_pedido': dados_pedido,
        'itens': itens,
        'total': total,
        'pedido': pedido,
    })

def acompanhar_pedido(request):
    pedido = None
    erro = None

    if request.method == 'POST':
        numero = request.POST.get('numero', '').strip()
        telefone = request.POST.get('telefone', '').strip()

        try:
            pedido = Pedido.objects.get(
                id=numero,
                telefone=telefone
            )
        except (Pedido.DoesNotExist, ValueError):
            erro = 'Pedido não encontrado. Confira o número e o telefone.'

    return render(request, 'loja/acompanhar_pedido.html', {
        'pedido': pedido,
        'erro': erro
    })



