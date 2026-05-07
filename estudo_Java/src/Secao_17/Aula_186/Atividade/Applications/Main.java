package Secao_17.Aula_186.Atividade.Applications;

import Secao_17.Aula_186.Atividade.entities.Caixa;

public class Main {
    public static void main(String[] args) {

        Caixa<String> caixaTexto = new Caixa<>();
        caixaTexto.guardar("Otto");

        System.out.println(caixaTexto.pegar());

        Caixa<Integer> caixaNumero = new Caixa<>();
        caixaNumero.guardar(8);

        System.out.println(caixaNumero.pegar());

    }
}
