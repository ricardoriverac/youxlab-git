package secao12_Enumerates.exercicioPropos.aplicacao;

import secao12_Enumerates.exercicioPropost.entities.*;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

import secao12_Enumerates.exercicioPropost.entities.OrderStatus;
import secao12_Enumerates.exercicioPropost.entities.Order;

public class program {
    public static void main(String[] args) throws ParseException {
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat fmt1 = new SimpleDateFormat("dd/MM/yyyy");


        List<Product> products= new ArrayList<>();
        List<OrderItem> orderItemList = new ArrayList<>();

        System.out.println("Enter cliente data: ");
        System.out.print("NOME: ");
        String nome = sc.nextLine();
        System.out.print("EMAIL: ");
        String email = sc.next();
        System.out.print("DATA DE NASCIMENTO: ");
        Date birthMonth = fmt1.parse(sc.next());
        Client client = new Client(nome, email, birthMonth);

        System.out.println("ENTER ORDER DATA: ");
        Order order = new Order();
        System.out.println("Order status: " + order.getStatus(OrderStatus.PROCESSING));
        System.out.print("How many items to this order? ");
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            System.out.printf("Enter order number %d data: \n", i);
            System.out.print("NAME: ");
            String nomeProd = sc.next();
            System.out.print("\nPrice: ");
            Double precoProd = sc.nextDouble();
            System.out.print("\nQuantity: ");
            int quantity = sc.nextInt();
            products.add(new Product(nomeProd, precoProd));
            orderItemList.add(new OrderItem(quantity, precoProd));
            Date moment = new Date();
            OrderStatus status = order.getStatus(OrderStatus.PROCESSING);
            order = new Order(moment, status);
        }
        System.out.print(order);
        sc.close();
    }
}
