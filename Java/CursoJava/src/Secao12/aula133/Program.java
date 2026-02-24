package Secao12.aula133;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Enter client data: ");
        System.out.print("Name: ");
        String name = sc.nextLine();

        System.out.print("Email: ");
        String email = sc.nextLine();

        System.out.print("Birth date (DD/MM/YYYY): ");
        LocalDate birthDate = LocalDate.parse(sc.nextLine(), fmt);

        Cliente cliente = new Cliente(name, email, birthDate);
        System.out.println("Enter order data:");
        System.out.print("Status: ");
        OrderStatus status = OrderStatus.valueOf(sc.next());

        Order order = new Order(LocalDateTime.now(), status, cliente);
        System.out.print("How many items to this order? ");
        int n = sc.nextInt();
        for (int i =1; i<=n; i++) {
            System.out.println("Enter contract #" + i + " item data:");
            sc.nextLine();

            System.out.print("Product Name: ");
            String productName = sc.nextLine();

            System.out.print("Product Price: ");
            double price = sc.nextDouble();

            System.out.print("Quantity: ");
            int quantity = sc.nextInt();

            Product product = new Product(productName, price);
            OrderItem item = new OrderItem(quantity, price, product);
            order.addItem(item);
        }
        System.out.println(order);
    }
}
