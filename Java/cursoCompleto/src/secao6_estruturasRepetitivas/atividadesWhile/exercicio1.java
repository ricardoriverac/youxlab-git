package secao6_estruturasRepetitivas.atividadesWhile;

import java.util.Scanner;

public class exercicio1 {
    public static void main(String[] args){
        // Declara scanner (serve como input)
        Scanner sc = new Scanner(System.in);
        // Declara a variável da senha com um valor fixo
        int senha = 2002;
        // Declara a variável da entrada com um valor scanner
        int entrada = sc.nextInt();
        // Começa uma estrutura while
        while (entrada != senha)
        //Define a condição de repetição, que deve se repetir até que a ENTRADA seja DIFERENTE da SENHA
        {
            System.out.println("ACESSO NEGADO");
            entrada = sc.nextInt();
        // Enquanto ENTRADA for DIFERENTE de SENHA, seá printada mensagem "ACESSO NEGADO"
        }
        // Quando a ENTRADA for IGUAL a SENHA, será printada a mensagem "ACESSO PERMITIDO" e o programa terminará
        System.out.println("ACESSO PERMITIDO");
        sc.close();
    }
}
