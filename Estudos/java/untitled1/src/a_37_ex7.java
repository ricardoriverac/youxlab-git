import java.util.Locale;
import java.util.Scanner;

public class a_37_ex7 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double eixoX, eixoY;

        System.out.print("Caro usuário, por favor digite o eixo X de seu plano cartesiano: ");
        eixoX = sc.nextDouble();
        System.out.print("Caro usuário, por favor digite o eixo Y de seu plano cartesiano: ");
        eixoY = sc.nextDouble();

        if (eixoX == 0 && eixoY == 0){
            System.out.printf("Caro usuário, tendo X como %.2f e Y como %.2f seu plano cartesiano está na origem", eixoX, eixoY);
        }
        else if(eixoX > 0 && eixoY < 0) {
            System.out.printf("Caro usuário, tendo X como %.2f e Y como %.2f seu plano cartesiano está na área Q4", eixoX, eixoY);
        }
        else  if (eixoX < 0 && eixoY > 0) {
            System.out.printf("Caro usuário, tendo X como %.2f e Y como %.2f seu plano cartesiano está na área Q2", eixoX, eixoY);
        }
        else if (eixoX < 0 && eixoY < 0) {
            System.out.printf("Caro usuário, tendo X como %.2f e Y como %.2f seu plano cartesiano está na área Q3", eixoX, eixoY);
        }
        else{
            System.out.printf("Caro usuário, tendo X como %.2f e Y como %.2f seu plano cartesiano está na área Q1", eixoX, eixoY);
        }
        sc.close();
    }
}
