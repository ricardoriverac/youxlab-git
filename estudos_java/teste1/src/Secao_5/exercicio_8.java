package Secao_5;
import java.util.Locale;
import java.util.Scanner;

public class exercicio_8 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double salary, tax;
        salary = sc.nextDouble();
        if (salary<=2000) {
            System.out.println("You are exempt from taxes");
        } else if (salary<3000) {
            salary -= 2000;
            tax = salary*0.08;
            System.out.printf("R$ %.2f", tax);
        } else if (salary<4500) {
            salary -= 3000;
            tax = 1000*0.08;
            tax += salary*0.18;
            System.out.printf("R$ %.2f", tax);
        } else {
            salary -= 4500;
            tax = 1000*0.08;
            tax += 1500*0.18;
            tax += salary*0.28;
            System.out.printf("R$ %.2f", tax);
        }
    }
}