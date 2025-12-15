import java.util.Scanner;

public class exercicio_3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a, b, c, d, diferenca;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        diferenca = ((a*b)-(c*d));

        System.out.printf("A diferença entre %d vezes %d e %d vezes %d é de %d", a, b, c, d, diferenca);
    }
}
