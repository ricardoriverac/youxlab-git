package Secao_10.Exercicio_06;

import java.util.Locale;
import java.util.Scanner;

public class multipleVectSum {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many numbers do you want to insert in each vect? ");
        int quantity = sc.nextInt();
        int[] vectA = new int[quantity];
        int[] vectB = new int[quantity];

        System.out.println("Enter some values into the vect A");
        for (int i=0 ; i<vectA.length ; i++) {
            vectA[i] = sc.nextInt();
        }
        System.out.println("Enter some values into the vect B");
        for (int i=0 ; i<vectB.length ; i++) {
            vectB[i] = sc.nextInt();
        }

        int[] finalVect = new int[quantity];
        System.out.println("Result Vect:");

        for (int i=0 ; i<quantity ; i++) {
            finalVect[i] = vectA[i] + vectB[i];
            System.out.println(finalVect[i]);
        }
    }
}
