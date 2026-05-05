package Secao_17.Aula_186.Generics.applications;

import Secao_17.Aula_186.Generics.entities.Repositorio;

public class Main {
    public static void main(String[] args) {

        Repositorio rp = new Repositorio();

        rp.salvar(4.009);
        System.out.println(rp.obter());
    }
}