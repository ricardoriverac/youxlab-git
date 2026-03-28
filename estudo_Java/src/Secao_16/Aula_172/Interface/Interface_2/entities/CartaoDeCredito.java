package Secao_16.Aula_172.Interface.Interface_2.entities;


import Secao_16.Aula_172.Interface.Interface_2.interfaces.Pagamento;

public class CartaoDeCredito implements Pagamento {

    @Override
    public void processar(double valor) {
        if (valor <= 0) {
            throw new IllegalArgumentException("Valor deve ser positivo");
        }
        System.out.printf("Pagamento de R$ %.2f no cartão de crédito%n", valor);
    }
}
