from django.contrib import admin
from chatbot_loja.models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'telefone',
        'entrega',
        'pagamento',
        'status',
        'total',
        'data_pedido',
    )

    list_filter = (
        'status',
        'pagamento',
        'entrega',
        'data_pedido',
    )

    search_fields = ('nome', 'telefone')
    inlines = [ItemPedidoInline]


admin.site.register(ItemPedido)