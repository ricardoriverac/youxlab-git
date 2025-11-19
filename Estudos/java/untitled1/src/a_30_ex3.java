import java.util.Scanner;

public class a_30_ex3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int fator1, fator2, fator3, fator4, produto1, produto2, diferenca;
        System.out.print("Digite o primeiro fator da expressão numérica: ");
        fator1 = sc.nextInt();
        System.out.print("Digite o segundo fator da expressão numérica: ");
        fator2 = sc.nextInt();
        System.out.print("Digite o terceiro fator da expressão numérica: ");
        fator3 = sc.nextInt();
        System.out.print("Digite o quarto fator da expressão numérica: ");
        fator4= sc.nextInt();


        produto1 = fator1 * fator2;
        produto2 = fator3 * fator4;

        diferenca = produto1 - produto2;
        System.out.printf("A diferença da multiplicação de %d e %d com a multiplicação de %d e %d é igual à %d", fator1, fator2, fator3, fator4, diferenca);
    }
}
