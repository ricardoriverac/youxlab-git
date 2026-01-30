package Secao_10.Exercicio_03.application;

import Secao_10.Exercicio_03.entities.Person;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many people will be entered into the registry?");
        int quantity = sc.nextInt();
        PersonManager manager = new PersonManager(quantity);
        manager.readPersons();
        manager.showAverageHeight();
        manager.showUnderage();
    }
}
