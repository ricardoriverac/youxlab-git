package Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.entities;

import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.interfacee.Pagamento;

public class Pedido {

    private final Pagamento pagamento;

    public Pedido(Pagamento pagamento) {
        this.pagamento = pagamento;
    }

    public void finalizarPedido(double valor) {
        pagamento.pagar(valor);
    }
}
