package secao_08.exercicio_1;

import java.util.Locale;
import java.util.Scanner;

public class programaPrincipal {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter rectangle widht and height: ");
        entities.widht = sc.nextDouble();
        entities.height = sc.nextDouble();

        System.out.println("Area = " + entities.area());
        System.out.println("Perimeter = " + entities.perimeter());
        System.out.println("Diagonal = " + entities.diagonal());

    }

}
