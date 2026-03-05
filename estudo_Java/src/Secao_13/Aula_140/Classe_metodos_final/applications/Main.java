package Secao_13.Aula_140.Classe_metodos_final.applications;

import Secao_13.Aula_140.Classe_metodos_final.entities.Carro;

public class Main {
    public static void main(String[] args) {

        Carro carro = new Carro("Fiat", "B-12", 20.00);

        carro.acelerar(22);
        carro.acelerar(11);

        System.out.println(carro.ligarArCondicionado());

        System.out.println(carro.exibirInformacoes());
    }
}
