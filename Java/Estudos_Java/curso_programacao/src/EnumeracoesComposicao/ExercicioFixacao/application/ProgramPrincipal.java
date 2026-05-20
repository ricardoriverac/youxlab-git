package EnumeracoesComposicao.ExercicioFixacao.application;

import EnumeracoesComposicao.ExercicioFixacao.entities.*;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class ProgramPrincipal {
    static void main() throws ParseException {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.println("Enter client data:");
        System.out.print("Name: ");
        String name = sc.nextLine();
        System.out.print("Email: ");
        String email = sc.next();
        System.out.print("Birth date (DD/MM/YYYY): ");
        Date birthDate = sdf.parse(sc.next());

        Client client = new Client(name, email, birthDate);

        System.out.println("Enter order data:");
        System.out.println("""
                PENDING_PAYMENT
                PROCESSING
                SHIPPED
                DELIVERED
                
                obs: DIGITE O MESMO DA TABELA
                """);
        System.out.print("Status: ");
        OrderStatus status = OrderStatus.valueOf(sc.next());
        Order order = new Order(new Date(), status, client);

        System.out.print("How many items to this order? ");
        int quantityItems = sc.nextInt();
        for (int i = 0; i < quantityItems; i++) {
            System.out.println("Enter #" + (i+1) + " item data:");
            System.out.print("Product name: ");
            String productName = sc.next();
            System.out.print("Product price: ");
            double price = sc.nextDouble();
            System.out.print("Quantity: ");
            int quantity = sc.nextInt();

            Product product = new Product(productName, price);
            OrderItem orderItem = new OrderItem(quantity, price, product);
            order.addItem(orderItem);
        }

        System.out.println();
        System.out.println("ORDER SUMMARY:");
        System.out.println(order);

        sc.close();

    }
}
