package Secao_10.Exercicio_03.application;

import Secao_10.Exercicio_03.entities.Person;

import java.util.Scanner;

public class PersonManager {

    private Person[] persons;

    public PersonManager(int quantity) {
        this.persons = new Person[quantity];
    }

    public void readPersons () {
        Scanner sc = new Scanner(System.in);

        for (int i=0 ; i<this.persons.length ; i++) {

            System.out.printf("%d°Person data: %n", i+1);
            System.out.print("Name: ");
            String ownName = sc.nextLine();

            System.out.print("Age: ");
            int ownAge = sc.nextInt();

            System.out.print("Height: ");
            double ownHeight = sc.nextDouble();

            persons[i] = new Person(ownName, ownAge, ownHeight);
            sc.nextLine();
        }
    }

    public void showAverageHeight() {

        double totalHeight = 0;
        for (int i = 0 ; i < this.persons.length ; i++) {
            totalHeight += persons[i].height;
        }
        System.out.println();
        System.out.printf("Average Height %.2f%n", totalHeight/persons.length);
    }

    public void showUnderage() {
        int underageCount = 0;

        for (int i = 0; i < this.persons.length; i++) {
            if (this.persons[i].underage) {
                underageCount += 1;
            }
        }
        System.out.println();
        System.out.printf("People below 16 years old: %.1f%s%n", (double)underageCount/this.persons.length*100, "%");

        for (int i = 0; i < this.persons.length; i++) {
            if (this.persons[i].age<16) {
                System.out.println(this.persons[i].name);
            }
        }
    }
}
