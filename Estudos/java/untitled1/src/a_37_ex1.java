import java.util.Scanner;

public class a_36 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        int numero;

        System.out.print("Caro usuário, por favor digite o valor desejado: ");
        numero = sc.nextInt();

        if(numero < 0){
            System.out.printf("O número %d é negativo!", numero);
        }
        else{
            System.out.printf("O número %d é positivo!", numero);
        }
    }
}
