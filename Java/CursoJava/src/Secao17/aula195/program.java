package Secao17.aula195;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> studentCodes = new HashSet<>();

        System.out.print("How many students for course A? ");
        int a = sc.nextInt();
        for (int i = 0; i < a; i++) {
            studentCodes.add(sc.nextInt());
        }

        System.out.print("How many students for course B? ");
        int b = sc.nextInt();
        for (int i = 0; i < b; i++) {
            studentCodes.add(sc.nextInt());
        }

        System.out.print("How many students for course C? ");
        int c = sc.nextInt();
        for (int i = 0; i < c; i++) {
            studentCodes.add(sc.nextInt());
        }

        System.out.println("Total students: " + studentCodes.size());
        sc.close();
    }
}

