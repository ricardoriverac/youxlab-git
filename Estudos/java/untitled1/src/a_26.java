import java.util.Scanner;

public class a_26 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String x;
        int y;
        double z;
        char x1;
        x = sc.next();
        y = sc.nextInt();
        z = sc.nextDouble();
        x1 = sc.next().charAt(0);
        System.out.println("Você digitou: " + x);
        System.out.println("Também digitou " + y);
        System.out.println("Mas também digitou " + z);
        System.out.println("A primeira caracter de sua string é: " + x1);
        int a1;
        double a2;
        String a3;
        a1 = sc.nextInt();
        a2= sc.nextDouble();
        a3= sc.next();
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);

        sc.close();
    }
}
