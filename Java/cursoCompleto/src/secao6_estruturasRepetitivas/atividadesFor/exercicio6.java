package secao6_estruturasRepetitivas.atividadesFor;

import java.util.Scanner;

public class exercicio6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int count = 0;
        for (int i = 0; i <=n; i++){
            count += 1;
            if (n % count == 0){
                System.out.println(count);
            }
        }

    }
}
