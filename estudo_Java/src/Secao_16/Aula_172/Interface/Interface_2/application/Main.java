package Secao_16.Aula_172.Interface.Interface_2.application;

import Secao_16.Aula_172.Interface.Interface_2.entities.Boleto;
import Secao_16.Aula_172.Interface.Interface_2.entities.CartaoDeCredito;
import Secao_16.Aula_172.Interface.Interface_2.entities.Pix;
import Secao_16.Aula_172.Interface.Interface_2.interfaces.Pagamento;

public class Main {
    public static void main(String[] args) {

        Pagamento[] pagamentos = {
                new CartaoDeCredito(),
                new Pix(),
                new Boleto(),
        };

        for (Pagamento p : pagamentos) {
            p.processar(150);
        }
    }
}
