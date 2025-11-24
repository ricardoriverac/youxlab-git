import java.util.Scanner;

public class a_37_ex4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int horaInicial, horaFinal;

        System.out.print("Caro usuário, por favor digite a hora inicial deste evento: ");
        horaInicial = sc.nextInt();
        System.out.print("Caro usuário, por favor digite a hora final deste evento: ");
        horaFinal = sc.nextInt();

        if (horaInicial >= horaFinal) {
            int duracao;
            duracao = (24 - horaInicial) + horaFinal;
            System.out.printf("A duração deste evento foi %d horas", duracao);
        }
        else{
            int duracao;
            duracao = horaFinal - horaInicial;
            System.out.printf("A duração deste evento foi %d horas", duracao);
        }
        sc.close();
    }
}
