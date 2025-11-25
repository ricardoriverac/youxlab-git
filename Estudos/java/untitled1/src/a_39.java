import java.util.Scanner;

public class a_39 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x;
        String dia;
        dia = "";

        System.out.print("Caro usuário, digite o dia da semana conforme sua posição [Ex: Domingo = 1]: ");
        x = sc.nextInt();

        /*
        if (x == 1) {
            dia = "Domingo";
        }
        else if (x == 2) {
            dia = "Segunda";
        }
        else if (x == 3){
            dia = "Terça-Feira";
        }
        else if (x == 4) {
            dia = "Quarta-Feira";
        }
        else if (x == 5) {
            dia = "Quinta-feira";
        }
        else if (x == 6) {
            dia = "Sexta-feira";
        }
        else if (x == 7){
            dia = "Sábado";
        }
        else {
            System.out.print("Dia inexistente");
        }
        */

        switch (x) {
            case 1:
                dia = "Domingo";
                break;
            case 2:
                dia = "Segunda-Feira";
                break;
            case 3:
                dia = "Terça-Feira";
                break;
            case 4:
                dia = "Quarta-Feira";
                break;
            case 5:
                dia = "Quinta-Feira";
                break;
            case 6:
                dia = "Sexta-Feira";
                break;
            case 7:
                dia = "Sábado";
                break;
            default:
                dia = "Valor inválido";
                break;
        }

        System.out.println("Dia da semana: " + dia);
        sc.close();
    }
}
