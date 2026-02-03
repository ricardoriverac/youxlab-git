package Secao_17.ExercicioFixacaoSet;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Program {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        Set<Integer> set3 = new HashSet<>();

        System.out.print("How many students for course A?");
        int quantity = sc.nextInt();
        for (int i = 0; i < quantity; i++) {
            set1.add(sc.nextInt());
        }

        System.out.print("How many students for course B?");
        quantity = sc.nextInt();
        for (int i = 0; i < quantity; i++) {
            set2.add(sc.nextInt());
        }

        System.out.print("How many students for course C?");
        quantity = sc.nextInt();
        for (int i = 0; i < quantity; i++) {
            set3.add(sc.nextInt());
        }

        Set<Integer> finalSet = new HashSet<>();
        finalSet.addAll(set1);
        finalSet.addAll(set2);
        finalSet.addAll(set3);
        System.out.println("Total students: " + finalSet.size());

    }

}
