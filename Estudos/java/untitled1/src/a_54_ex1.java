import java.util.Scanner;

public class a_54_ex1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numeroLimite;
        System.out.print("Caro usuário, digite quantos números ímpares  você deseja imprimir: ");
        numeroLimite = sc.nextInt();
        for(int i=1;i<=numeroLimite; i++){
            if (i % 2 != 0){
                System.out.println(i);
            }
            sc.close();
        }
    }
}
