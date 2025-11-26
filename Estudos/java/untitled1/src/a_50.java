import java.util.Scanner;


public class a_50 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;
        numero = sc.nextInt();
        int soma = 0;

        for(int i=0;i<numero;i++){
            int x = sc.nextInt();
            soma = soma+x;
        }
        System.out.println(soma);
    }
}
