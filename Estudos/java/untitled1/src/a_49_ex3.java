import java.util.Scanner;

public class a_49_ex3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String menu;
        int codigo, countGasolina, countAlcool, countDiesel;
        countGasolina = 0;
        countAlcool = 0;
        countDiesel = 0;
        codigo = 0;

        menu =  "MENU POSTO\n"
                +"1-ÁLCOOL\n"
                +"2-GASOLINA\n"
                +"3-DIESEL\n"
                +"4-FIM\n";
        while (codigo != 4){
                System.out.println("Caro usuário, selecione o seu produto favorito, escolhendo o id de cada opção de nosso Menu");
                System.out.print(menu);
                codigo = sc.nextInt();

            switch (codigo){
                case 1 :
                    countAlcool += 1;
                    System.out.print("Preferência registrada! ");

                case 2:
                    countGasolina += 1;
                    System.out.print("Preferência registrada! ");
                case 3:
                    countDiesel+=1;
                    System.out.print("Preferência registrada! ");
                default:
                    System.out.println("Caro usuário, selecione um código válido de nosso menu");
                    System.out.print(menu);
                    codigo = sc.nextInt();
            }
        }
        System.out.printf("Álcool: %d\n " + "Gasolina: %d\n" + "Diesel: %d\n", countAlcool, countGasolina, countDiesel);
        sc.close();
    }

}
