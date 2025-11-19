import java.util.Scanner;

public class a_30_ex2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double raio, pi, area;

        System.out.print("Digite o raio do círculo");
        raio = sc.nextDouble();
        pi = 3.14159;
        area = pi * (Math.pow(raio, 2));
        System.out.printf("A área do círculo é %f", area);
    }
}
