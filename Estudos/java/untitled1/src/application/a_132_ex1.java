import application.entities.*;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class a_132_ex1 {
    public static void main(String[] args) throws ParseException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.print("Caro cliente, por favor insira seu nome para cadastro: ");
        String nome = sc.nextLine();
        System.out.print("Caro cliente, por favor insira seu email para cadastro: ");
        String email = sc.nextLine();
        System.out.print("Caro cliente, por favor insira sua data de nascimento para cadastro: (dd/MM/yyyy)");
        Date nascimentoCliente = sdf.parse(sc.next());
        Cliente clientes = new Cliente(nome, email, nascimentoCliente);

        System.out.println("Caro cliehte, por favor insira o status de seu pedido: ");
        OrderStatus statusPedido = OrderStatus.valueOf(sc.next());
        Pedido2 pedido = new Pedido2(new Date(), statusPedido, clientes);
        System.out.print("Caro cliente, por favor insira qual a quantidade de produtos em seu pedido: ");
        int quantidadeProdutos = sc.nextInt();
        for (int i = 0; i < quantidadeProdutos; i++) {
            System.out.printf("Caro cliente, por favor insira o nome do %do produto", i+1);
            String nomeProduto = sc.nextLine();
            sc.next();
            System.out.printf("Caro cliente, por favor insira o preço do %do produto", i+1);
            Double precoProduto = sc.nextDouble();
            Produto produtos = new Produto(nomeProduto, precoProduto);
            System.out.printf("Caro cliente, por favor insira a quantidade de %s encomendada", nomeProduto);
            Integer quantidadeItens = sc.nextInt();
            ItensPedido itensPedido = new ItensPedido(quantidadeItens, precoProduto, produtos);
            pedido.addItens(itensPedido);
        }
        System.out.println(pedido);

    }
}

