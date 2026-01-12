package application;

import java.util.InputMismatchException;
import java.util.Scanner;

public class a_151 {
    public static void main(String[] args) {
        method1();

        System.out.print("Fim do programa! ");
    }
    public static void method1(){
        System.out.print("***METHOD 1 START***");
        method2();
        System.out.print("***METHOD 1 END***");
    }
    public static void method2(){
        System.out.print("***METHOD 2 START***");
        Scanner sc = new Scanner(System.in);

        try{
            String[] vect = sc.nextLine().split(" ");
            int posicao = sc.nextInt();
            System.out.print(vect[posicao]);
        }
        catch (ArrayIndexOutOfBoundsException e){
            System.out.print("Posicao invalida");
            e.printStackTrace();
            sc.next();
        }
        catch (InputMismatchException e){
            System.out.print("Erro de input");
        }
        sc.close();
        System.out.print("***METHOD2 END***");
    }
}
