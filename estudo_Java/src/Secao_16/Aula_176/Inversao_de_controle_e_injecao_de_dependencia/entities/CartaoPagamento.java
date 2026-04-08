package Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.entities;

import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.interfacee.Pagamento;

public class CartaoPagamento implements Pagamento {

    @Override
    public void pagar(double valor) {
        System.out.println("Pagamento pelo Cartão: " + valor);
    }
}
