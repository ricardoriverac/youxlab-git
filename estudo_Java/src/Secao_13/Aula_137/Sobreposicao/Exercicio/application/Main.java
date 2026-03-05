package Secao_13.Aula_137.Sobreposicao.Exercicio.application;

import Secao_13.Aula_137.Sobreposicao.Exercicio.entities.Boleto;
import Secao_13.Aula_137.Sobreposicao.Exercicio.entities.CartaoCredito;
import Secao_13.Aula_137.Sobreposicao.Exercicio.entities.Pagamento;
import Secao_13.Aula_137.Sobreposicao.Exercicio.entities.Pix;

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
