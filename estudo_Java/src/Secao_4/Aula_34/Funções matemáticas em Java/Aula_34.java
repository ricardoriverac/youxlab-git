import java.util.Scanner;

public class Aula_34 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        System.out.print("Digite um número: ");
        double a = sc.nextDouble();
        double r = Math.sqrt(a);
        System.out.print("A raiz quadrada de " + a + " = " + r);



        sc.close();
    }
    
}
