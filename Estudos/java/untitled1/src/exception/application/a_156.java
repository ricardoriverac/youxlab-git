package exception.application;

import exception.entities.Reserva;
import exception.exception.DomainException;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class a_156 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        try {
            System.out.print("Número do quarto: ");
            int numero = sc.nextInt();
            System.out.print("Data de check-in: ");
            Date checkIn = sdf.parse(sc.next());
            System.out.print("Check - out date (dd/MM/yyyy");
            Date checkOut = sdf.parse(sc.next());

            Reserva reserva = new Reserva(numero, checkIn, checkOut);
            System.out.print("Reserva: " + reserva);
            System.out.println();
            System.out.print("Insira a data atualizada da reserva: \n");
            System.out.print("Data de check-in (dd/MM/yyyy): ");
            checkIn = sdf.parse(sc.next());
            System.out.print("Data de check-out (dd/MM/yyyy): ");
            checkOut = sdf.parse(sc.next());

            reserva.atualizarData(checkIn, checkOut);
            System.out.print("Reserva: " + reserva);
        }
        catch (ParseException e){
            System.out.print("Formato de data inválido");
        }
        catch (DomainException e){
            System.out.print("Erro na reserva: " + e.toString());
        }
        catch (RuntimeException e){
            System.out.print("Erro inesperado");
        }
        sc.close();


    }
}
