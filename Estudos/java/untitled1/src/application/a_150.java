package application;

import java.util.InputMismatchException;
import java.util.Scanner;

public class a_150 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try{
            String[] vect = sc.nextLine().split(" ");
            int posicao = sc.nextInt();
            System.out.println(vect[posicao]);
        }

        catch (ArrayIndexOutOfBoundsException e){
            System.out.print("Posição inválida");
        }
        catch (InputMismatchException e){
            System.out.print("Erro de input");
        }
        System.out.print("Fim do programa! ");
    }
}
