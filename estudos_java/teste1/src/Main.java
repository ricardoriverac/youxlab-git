/* import java.util.List;
*  import java.util.Locale;
*  import java.util.Scanner;*/

public class Main {
    public static void main(String[] args){

        double x = 3.0;
        double y = 4.0;
        double z = -5.0;
        double A, B, C;

        A = Math.sqrt(x);
        B = Math.sqrt(y);
        C = Math.sqrt(25.0);
        System.out.println("Raiz quadrada de " + x + " = " + A);
        System.out.println("%Raiz quadrada de " + y + " = " + B);
        System.out.println("Raiz quadrada de 25 = " + C);

        A = Math.pow(x, y);
        B = Math.pow(x, 2.0);
        C = Math.pow(5.0, 2.0);
        System.out.println(x + " elevado a " + y + " = " + A);
        System.out.println(x + " elevado ao quadrado = " + B);
        System.out.println("5 elevado ao quadrado = " + C);

        A = Math.abs(y);
        B = Math.abs(z);
        System.out.println("Valor absoluto de " + y + " = " + A);
        System.out.println("Valor absoluto de " + z + " = " + B);

    }
}

/* %n quebra linha
*  %f float
*  %s string
*  %d int
*
*  print escreve sem formatação e quebra de linha
*  printf escreve com formatação
*  println escreve e faz a quebra de linha
*
*  Boa Prática:
*  Colocar .0 em variáveis double, ex: 9.0
*  Colocar f em variáveis float, ex: 9f
*
*  Locale define se a variável vai ser com "." ou ","
*
* Código do Scanner:
*  Scanner sc = new Scanner(System.in)
*  Next você tem que diferenciar se é Int, Float, Double
*  charAt exibe o caracter que
*  nextLine para frase
*
*  Sintaxe do switch-case:
*
*  switch ( expressão ) {
*   case valor1:
*       comando1
*       comando2
*       break;
*   case valor2:
*       comando3
*       comando4
*       break;
*   default:
*       comando5
*       comando6
*       break;
*  }
*
*  Expressão condicional ternária:
*
* Sintaxe:
*  ( condição ) ? valor se verdadeiro : valor se falso
* Exemplos:
*  price = ( 2 > 4 ) ? 50 : 80 → 80
*  name = ( 10 != 3 ) ? "Maria" : "Alex" → "Maria"
*
* do-while:
* Sintaxe:
* do {
* comando 1
* comando 2
* } while (condição)
* Ele realiza o while pelo menos uma vez.
* Obs: Muito pouco utilizado
* */








