import java.util.Scanner;


public class a_54_ex2 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

        int limite;
        System.out.print("Caro usuário, digite quantos números você deseja inserir, verificando o intervalo de 10 a 20");
        limite = sc.nextInt();

        for(int i=1; i<=limite;i++) {
            int numero;
            System.out.print("Caro usuário, por favor insira o número que você deseja verificar");
            numero = sc.nextInt();
            if (numero <10 || numero >20){
                System.out.printf("%d out\n", numero);
            }
            else if (numero >=10 && numero <=20){
                System.out.printf("%d in\n", numero);
            }
        }

    }
}
