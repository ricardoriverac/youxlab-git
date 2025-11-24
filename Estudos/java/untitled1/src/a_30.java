import java.util.Scanner;

public class a_30 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        int parcela1, parcela2, soma;
        parcela1 = sc.nextInt();
        parcela2 = sc.nextInt();
        soma = parcela1 + parcela2;
        System.out.printf("Soma = %d", soma);
        sc.close();
    }
}
