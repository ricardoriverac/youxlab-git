package Secao_13.Aula_139.Exercicio.Sobreposicao.entities.application;

import Secao_13.Aula_139.Exercicio.Sobreposicao.entities.Boleto;
import Secao_13.Aula_139.Exercicio.Sobreposicao.entities.CartaoCredito;
import Secao_13.Aula_139.Exercicio.Sobreposicao.entities.Pagamento;
import Secao_13.Aula_139.Exercicio.Sobreposicao.entities.Pix;

public class Main {
    public static void main(String[] args) {

        Pagamento p1 = new CartaoCredito(1000);
        Pagamento p2 = new Boleto(1000);
        Pagamento p3 = new Pix(1000);

        System.out.println(p1.calcularValorFinal());
        System.out.println(p2.calcularValorFinal());
        System.out.println(p3.calcularValorFinal());
    }
}
