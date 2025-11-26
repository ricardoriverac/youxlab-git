import java.util.Scanner;
import java.util.Locale;

public class a_49_ex2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        double x, y;

        System.out.print("Caro usuário, por favor digite a coordenada do eixo X: ");
        x = sc.nextDouble();
        System.out.print("Caro usuário, por favor digite a coordenada do eixo Y: ");
        y = sc.nextDouble();

        while (x == 0 && y == 0){
            System.out.println("Caro usuário, por favor digite os eixos tendo suas coordenadas não nulas");
            System.out.print("Caro usuário, por favor digite a coordenada do eixo X: ");
            x = sc.nextDouble();
            System.out.print("Caro usuário, por favor digite a coordenada do eixo Y: ");
            y = sc.nextDouble();
        }

        while (x != 0 && y != 0){
            if (x > 0 && y > 0) {
                System.out.print("Caro usuário, seu plano cartesiano se encontra no quadrante 1");
                break;
            }
            else if (x < 0 && y >0 ){
                System.out.print("Caro usuário, seu plano cartesiano se encontra no quadrante 2");
                break;
            }
            else if (x < 0 && y < 0){
                System.out.print("Caro usuário, seu plano cartesiano se encontra no quadrante 3");
                break;
            }
            else if (x > 0 && y < 0) {
                System.out.print("Caro usuário, seu plano cartesiano se encontra no quadrante 4");
                break;
            }
            else {
                System.out.print("Caro usuário, por favor digite os eixos tendo suas coordenadas não nulas");
                break;
            }
        }
    }
}
