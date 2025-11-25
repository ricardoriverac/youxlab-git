import java.util.Scanner;

public class a_49_ex1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int senha;
        System.out.print("Caro usuário, por favor digite sua senha: ");
        senha = sc.nextInt();

        while (senha != 2002) {
            System.out.print("Caro usuário, por favor digite sua senha de forma correta: ");
            senha = sc.nextInt();
        }
        System.out.print("Acesso permitido!");
        sc.close();
    }
}
