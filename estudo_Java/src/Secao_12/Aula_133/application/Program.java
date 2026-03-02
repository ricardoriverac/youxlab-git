package Secao_12.Aula_133.application;

import Secao_12.Aula_133.Enum.OrderStatus;
import Secao_12.Aula_133.entitis.Client;
import Secao_12.Aula_133.entitis.Order;
import Secao_12.Aula_133.entitis.OrderItem;
import Secao_12.Aula_133.entitis.Product;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) throws ParseException {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Date date = new Date();

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.println("Enter cliente data: ");

        System.out.print("Name: ");
        String name = sc.nextLine();

        System.out.print("Email: ");
        String email = sc.next();

        System.out.print("Birth date (DD/MM/YYYY): ");
        Date birthDate = sdf.parse(sc.next());

        System.out.print("Status: ");
        String status = sc.next().toString();


        Order order = new Order(date, OrderStatus.valueOf(status), new Client(name, email, birthDate));

        System.out.print("How many items to this order? ");
        int quantityOrder = sc.nextInt();

        for (int i = 0; i < quantityOrder; i++) {
            System.out.printf("Enter #%d item data: %n", (1+i));

            System.out.print("Product name: ");
            String productName = sc.next();

            System.out.print("Product price: ");
            double productPrice = sc.nextDouble();

            System.out.print("Quantity: ");
            int quantity = sc.nextInt();

            OrderItem orderItem = new OrderItem(quantity, productPrice, new Product(productName, productPrice));
            order.addItem(orderItem);
        }

        System.out.println(order.toString());
    }
}
