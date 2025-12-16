package Secao_5;

import java.util.Scanner;
import java.util.Locale;

public class exercicio_4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int idemployee = sc.nextInt();
        double wagePerHour = sc.nextDouble();
        double hour = sc.nextDouble();
        double salary = wagePerHour * hour;

        System.out.printf("EMPLOYEE ID NUMBER = %s",idemployee);
        System.out.printf("%nSALARY = U$ %.2f",salary);
    }
}
