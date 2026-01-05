package secao6_estruturasRepetitivas.atividadesWhile;

import java.util.Scanner;
public class exercicio3 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("< ESCOLHA UM ITEM > \nAlcool: 1\nGasolina: 2\nDiesel: 3\n<DIGITE 4 PARA PARAR O PROGRAMA>\nDigite o ITEM que você deseja: ");
        int entrada = sc.nextInt();
        int alcool = 0;
        int gasolina = 0;
        int diesel = 0;
        while(entrada != 4){
            System.out.println("< ESCOLHA UM ITEM > \nAlcool: 1\nGasolina: 2\nDiesel: 3\n<DIGITE 4 PARA PARAR O PROGRAMA>\nDigite o ITEM que você deseja: ");
            if (entrada == 1){
                alcool += 1;
            }
            else if (entrada == 2){
                gasolina += 1;
            }
            else if (entrada == 3) {
                diesel += 1;
            }
            else {
                System.out.println("<NÃO RECONHECIDO>");
            }
            entrada = sc.nextInt();

        }
        System.out.printf("< NÚMERO DE CLIENTES POR PRODUTO >\nAlcool: ", alcool, "\nGasolina: ", gasolina, "\nDiesel: ", diesel);
        System.out.println("<FIM DO PROGRAMA>");
    }
}
