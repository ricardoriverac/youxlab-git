package secao6_estruturasRepetitivas.atividadesWhile;
import java.util.Scanner;
public class exercicio2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int CordX = sc.nextInt();
        int CordY = sc.nextInt();

        while (CordX != 0 && CordY != 0) {
            if (CordX > 0 && CordY > 0) {
                System.out.println("Primeiro Quadrante");
            }
            else if (CordX < 0 && CordY > 0) {
                System.out.println("Segundo Quadrante");
            }
            else if (CordX < 0 && CordY < 0) {
                System.out.println("Terceiro Quadrante");
            }
            else {
                System.out.println("Quarto Quadrante");
            }
            CordX = sc.nextInt();
            CordY = sc.nextInt();
        }
        System.out.println("< Não Identificado >");
    }
}
