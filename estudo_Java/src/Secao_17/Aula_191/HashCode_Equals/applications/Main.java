package Secao_17.Aula_191.HashCode_Equals.applications;

import Secao_17.Aula_191.HashCode_Equals.entities.Client;

public class Main {
    public static void main(String[] args) {

        Client c1 = new Client("Elisangela", "elisangela@gmail.com");
        Client c2 = new Client("Patricia", "patricia123@gmail.com");

        System.out.println("hashCode -> " + c1.hashCode());
        System.out.println("hashCode -> " + c2.hashCode());

        System.out.println("equals -> " + c1.equals(c2));
    }
}
