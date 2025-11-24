import java.util.Scanner;

public class a_37_ex3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero1, numero2;

        System.out.print("Caro usuário, por favor digite o primeiro valor desejado: ");
        numero1 = sc.nextInt();
        System.out.print("Caro usuário, por favor digite o segundo valor desejado: ");
        numero2 = sc.nextInt();
        if (numero1 % numero2 == 0 || numero2 % numero1 == 0 ) {
            System.out.printf("Os números %d e %d são múltiplos", numero1, numero2);
        }
        else{
            System.out.printf("Os números %d e %d não são múltiplos", numero1, numero2);
        }
        sc.close();
    }
}
