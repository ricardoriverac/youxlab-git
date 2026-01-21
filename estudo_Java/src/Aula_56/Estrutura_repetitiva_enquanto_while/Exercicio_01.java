package Aula_56.Estrutura_repetitiva_enquanto_while;

import java.util.Scanner;

public class Exercicio_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a senha: ");
        int Valor_Senha = sc.nextInt();

        while (Valor_Senha != 2002){
            System.out.print("Senha incorreta, digite novamente: ");
            Valor_Senha = sc.nextInt();
        }
        System.out.println("Acesso Permitido!!");
    }
}