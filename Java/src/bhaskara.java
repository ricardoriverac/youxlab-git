import java.util.Scanner;
public class bhaskara {
    public static void bhaskara(String[] args) {
        Scanner sc = new Scanner(System.in);
        float delta, x1, x2, a, b, c;

        a = sc.nextFloat();
        b = sc.nextFloat();
        c = sc.nextFloat();
        delta = (float) Math.pow(b, 2.0) - 4 * a * c;
        x1 =(float) (-b +  Math.sqrt(delta)) / (float)(2.0 * a);
        x2 = (float)(-b - Math.sqrt(delta)) / (float)(2.0 * a);
        System.out.printf("O delta é ", delta);
        System.out.printf("O x1 é ", x1);
        System.out.printf("O x2 é", x2);
    }
}
