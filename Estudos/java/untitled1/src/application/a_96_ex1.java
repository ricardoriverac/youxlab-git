package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex1 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Caro usuário, insira quantos números você deseja verificar [0 a 10]");
        int limite = sc.nextInt();
        if (limite>10) {
            System.out.println("Caro usuário, por favor escolha um limite válido[0 a 10]");
            System.out.println("Caro usuário, insira quantos números você deseja verificar [0 a 10]");
            limite = sc.nextInt();
        }
        int[] vect = new int[limite];
        for (int i = 0; i < vect.length; i++) {
            System.out.printf("Caro usuário, por favor insira um dos %d números", vect.length);
            vect[i]= sc.nextInt();
        }
        System.out.println("Números negativos: ");
        for(int i = 0; i<vect.length; i++){
            if (vect[i] < 0){
                System.out.printf("%d\n", vect[i]);
            }
        }
        sc.close();
    }
}
