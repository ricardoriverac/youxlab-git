package Secao_16.Aula_172.Interface.Interface_1.applications;

import Secao_16.Aula_172.Interface.Interface_1.entites.Circulo;
import Secao_16.Aula_172.Interface.Interface_1.entites.Quadrado;
import Secao_16.Aula_172.Interface.Interface_1.interfaces.Forma;

public class Main {
    public static void main(String[] args) {

        Forma f1 = new Circulo(2.0);
        Forma f2 = new Quadrado(4.0);

        System.out.println("Circulo: " + f1.calcularArea());
        System.out.println("Quadrado: " + f2.calcularArea());
    }
}
