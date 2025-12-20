package secao_10.aula96.Exerciciofixa.DesafioVetores.CodigoPrincipal;

import secao_10.aula96.Exerciciofixa.DesafioVetores.EntidadeVET.Estudante;

import java.util.Scanner;

public class PrincipalCOD {
    static void main() {

        Scanner sc = new Scanner(System.in);
        System.out.print("How many rooms will be rented? ");

        int qntQuartos = sc.nextInt();
        Estudante boardingHouse =  new Estudante();
        String[] rooms = new String[qntQuartos];

        for (int i = 0; i < qntQuartos; i++) {
            System.out.println("Rent #" + (i+1));
            System.out.print("Name: ");
            boardingHouse.setEstudante(sc.next());
            System.out.print("Email: ");
            boardingHouse.setEmail(sc.next());
            System.out.print("Room: ");
            boardingHouse.setRooms(sc.nextInt());
            rooms[i] = boardingHouse.toString();
            System.out.println();

        }

        System.out.println("Busy rooms:");
        for (int i = 0; i < rooms.length; i++) {
            System.out.println(rooms[i]);
        }

        sc.close();


            }
        }

