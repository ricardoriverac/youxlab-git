import java.util.Scanner;
import java.util.Locale;

public class a_37_ex8 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Locale.setDefault(Locale.US);

    float salario;
        System.out.print("Caro usuário, por favor insira o seu salário: ");
        salario = sc.nextFloat();

        if (salario <= 2000) {
            System.out.print("Caro usuário, você está isento do Imposto de Renda");
        }
        else if (salario > 2000 && salario <= 3000) {
            float ir;
            ir = (salario - 2000) * 0.08f;
            System.out.printf("Você terá que pagar %f de imposto de renda", ir);
        }
        else if (salario > 3000 && salario < 4500){
            float ir, faixa1, faixa2, faixa3;
            // 3002
//          faixa1 = 1002
            faixa1 = salario - 2000;
//          faixa = 2
            faixa2 = faixa1 - 1000;
            ir = (faixa1-faixa2) * 0.08f;
            ir = ir + (faixa2 * 0.18f);
            System.out.printf("Caro usuário, você terá que pagar %.2f de imposto de renda", ir);

        }
        else{
            float ir, faixa1, faixa2, faixa3;
            // 3002
//          faixa1 = 1002
            faixa1 = salario - 2000;
//          faixa = 2
            faixa2 = faixa1 - 1000;
            ir = (faixa1-faixa2) * 0.08f;
            ir = ir + (faixa2 * 0.18f);
            faixa3 = faixa1 - 2500;
            ir = ir + (faixa3 * 0.25f);
            System.out.printf("Caro usuário, você terá que pagar %.2f de imposto de renda", ir);
        }

    }
}
