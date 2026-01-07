package secao6_estruturasRepetitivas.atividadesFor;

import java.util.Scanner;

public class exercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int fat = 1;//  cada volta, significará uma diferença no fatorial, até chegar no número desejado
        for (int i = 0; i <= n; i++){
            fat *= i;
            //8! = 8 * 7 * 6 ... * 1
            //         (8-1) * (8-2)
            //         (7*1) * (6*1)
            //          <SÉTIMA VOLTA> * <SEXTA VOLTA>
        }

    }
}
