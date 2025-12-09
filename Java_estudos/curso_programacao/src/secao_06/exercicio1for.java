package secao_06;

import java.util.Scanner;

public class exercicio1for {
    static void main() {
        System.out.println("Digite um número inteiro");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        for(int i=1; i<=x; i++) {
            if(i % 2 != 0){
                System.out.println("Os valores impares são: "+ i);
            }
            sc.close();
        }
    }
}
