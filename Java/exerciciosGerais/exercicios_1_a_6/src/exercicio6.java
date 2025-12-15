import java.util.Scanner;
import static java.lang.Math.pow;
public class exercicio6 {
    public static void main(String[] args) {
        double A, B, C, areaTri, areaQuad, areaRet, areaCirc, areaTrap, pi;
        Scanner sc = new Scanner(System.in);

        pi = 3.14159;
        A = sc.nextDouble();
        B = sc.nextDouble();
        C = sc.nextDouble();
        areaTri = (A * C)/2;
        areaCirc = pow(C, 2) * pi;
        areaTrap = (A - B) * C/2;
        areaQuad =  pow(C, 4);
        areaRet = A * B;

        System.out.println("TRIÂNGULO: " + areaTri + "\nCÍRCULO: " + areaCirc + "\nTRAPÉZIO: " + areaTrap + "\nQUADRADO: " + areaQuad + "\nRETÂNGULO: " + areaRet);
        sc.close();
    }
}
