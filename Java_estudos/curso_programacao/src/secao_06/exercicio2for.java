package secao_06;

import java.util.Scanner;

public class exercicio2for {
    static void main() {

        System.out.println("Digite um valor inteiro: ");
        Scanner sc = new Scanner(System.in);
        int qtd_leituras = sc.nextInt();
        int numero, dentro_faixa = 0, fora_faixa = 0;


        for (int i=0; i<qtd_leituras; i++){
            numero = sc.nextInt();
            if ( numero <= 20 && numero >= 10){
                dentro_faixa++;
            }else {
                fora_faixa++;
            }

        }
        System.out.println(dentro_faixa + " in");
        System.out.println(fora_faixa + " out");
        sc.close();
    }
}
