package Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.applications;

import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.entities.BoletoPagamento;
import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.entities.CartaoPagamento;
import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.entities.Pedido;
import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.entities.PixPagamento;
import Secao_16.Aula_176.Inversao_de_controle_e_injecao_de_dependencia.interfacee.Pagamento;

public class Main {
    public static void main(String[] args) {

        Pagamento p = new CartaoPagamento();
        Pedido pdd = new Pedido(p);

         pdd.finalizarPedido(200.00);
    }
}
