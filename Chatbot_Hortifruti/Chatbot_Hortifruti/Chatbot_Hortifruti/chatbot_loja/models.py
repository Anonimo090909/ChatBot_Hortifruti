from django.db import models


class Pedido(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    entrega = models.CharField(max_length=20)
    endereco = models.TextField(blank=True)
    pagamento = models.CharField(max_length=30)

    status = models.CharField(
        max_length=30,
        choices=[
            ('pendente', 'Pendente'),
            ('preparando', 'Em preparação'),
            ('saiu_entrega', 'Saiu para entrega'),
            ('entregue', 'Entregue'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendente'
    )

    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.nome} - R$ {self.total}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    produto = models.CharField(max_length=150)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.quantidade} unidade(s)"