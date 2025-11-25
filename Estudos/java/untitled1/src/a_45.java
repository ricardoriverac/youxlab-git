import java.util.Scanner;

public class a_45 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, por favor digite o valor desejado! [0] para sair");
        int x = sc.nextInt();
        int soma = 0;

        while (x != 0) {
            soma += x;
            System.out.print("Caro usuário, por favor digite o valor desejado! [0] para sair");
            x = sc.nextInt();
            System.out.print(soma);
        }
        sc.close();
    }
}
