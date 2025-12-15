package secao_09.EXercicioDeFixacao.ProgA88;

import secao_09.EXercicioDeFixacao.ProgA88.EntitiesA88.acontsbank;

import java.util.Locale;
import java.util.Scanner;

public class programaPrincipal {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter account number: ");
        int number = sc.nextInt();
        
        System.out.println("Enter account holder: ");
        String holder = sc.next();
        acontsbank acc = new acontsbank(holder, number);

        System.out.println("Is there na initial deposit (y/n)? ");
        char resposta = sc.next().charAt(0);
        double initialDeposit;
        if(resposta == 'y'){
            System.out.println("Enter a deposit value:");
            initialDeposit = sc.nextDouble();
            acc.deposit(initialDeposit);

        }else {
            acontsbank acconts = new acontsbank(holder, number);
        }


        System.out.println("Account data: ");
        System.out.printf("Accont: %d, Holder: %s, Balence: $ %.2f", acc.getNumber(),acc.getHolder(), acc.getBalence());
        System.out.println();
        System.out.println("Enter a deposit value: ");
        initialDeposit = sc.nextDouble();
        acc.deposit(initialDeposit);
        System.out.println("Updated account data: ");
        System.out.printf("Account: %d, Holder: %s, Balance: $ %.2f", acc.getNumber(), acc.getHolder(), acc.getBalence());
        System.out.println();
        System.out.println("Enter a withdraw value: ");
        double remove = sc.nextDouble();
        acc.withDraw(remove);
        System.out.println("Updated account data: ");
        System.out.printf("Account : %d, Holder: %s, Balance: $ %.2f", acc.getNumber(), acc.getHolder(), acc.getBalence());



        sc.close();
    }
}
