import java.util.Scanner;

public class Aula_32 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); /*Diz ao java quando podemos usar o Scanner*/

        // Scanner String
        String x;
        x = sc.next(); /* O sc.next, serve somente para strings */
        System.out.print("Meu nome: " + x);

        // Scanner Int
        int y;
        y = sc.nextInt();/*O sc.nextInt, recebe somente números inteiros*/
        System.out.print("Minha idade: " + y);

        // Scanner Double
        double z;
        z = sc.nextDouble(); /*recebe números inteiros*/
        System.out.println("Número com virgula: " + z);

        // Scanner char
        char o;
        o = sc.next().charAt(0);/*O sc.next(),charAt(0), só pega a primeira letra da palavra*/
        System.out.println("1° letra: " + o);

        // Scanner que le a frase inteira
        String a;
        a = sc.nextLine();
        System.out.println("Frase -> " + a);



        sc.close();/*Diz para o java quando não podemos mais usar o Scanner*/
    }
}
