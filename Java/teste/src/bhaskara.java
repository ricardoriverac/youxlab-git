import java.util.Scanner;

public class bhaskara {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double delta, x1, x2, a, b, c;

        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();
        delta = Math.pow(b, 2.0) - 4 * a * c;
        x1 =(-b +  Math.sqrt(delta)) / (2.0 * a);
        x2 = (-b - Math.sqrt(delta)) / (2.0 * a);
        System.out.println("O delta é " + delta);
        System.out.println("\nO x1 é " + x1);
        System.out.println("\nO x2 é " + x2);
    }
}
