import application.POO.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

import static application.POO.Status.EM_ANDAMENTO;

public class desafioPOO {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int menu = 0;
        List<Produto> list = new ArrayList<>();
        List<Pedido> pedidosGerais = new ArrayList<>();
        Cliente clienteCadastrado = null;
        Endereco enderecos = null;
        Status statusPedido = null;

        while (menu != 5) {
            System.out.println("\nCaro usuário, escolha uma das opções de nosso menu: ");
            System.out.println("1- Cadastrar novo cliente\n"
                    + "2-Realizar pedido\n"
                    + "3- Buscar pedido por ID\n"
                    + "4- Buscar pedido por Status\n"
                    + "5- Sair");

            menu = sc.nextInt();

            switch (menu) {

                case 1:
                    System.out.print("Caro usuário, por favor informe o id do(a) cliente: ");
                    Integer idCliente = sc.nextInt();
                    sc.nextLine();

                    System.out.print("\nCaro usuário, por favor informe o nome do(a) cliente: ");
                    String nomeClientes = sc.nextLine();

                    System.out.printf("Caro usuário, por favor informe o email do(a) cliente %s: ", nomeClientes);
                    String email = sc.nextLine();

                    Cliente clientes = new Cliente(idCliente, nomeClientes, email);
                    clienteCadastrado = clientes;

                    System.out.printf("\nCaro usuário, por favor informe a rua do(a) cliente %s: ", nomeClientes);
                    String rua = sc.nextLine();

                    System.out.printf("\nCaro usuário, por favor informe o número da residência do(a) cliente %s: ", nomeClientes);
                    String numero = sc.nextLine();

                    System.out.printf("\nCaro usuário, por favor informe a cidade do(a) cliente %s: ", nomeClientes);
                    String cidade = sc.nextLine();

                    System.out.printf("\nCaro usuário, por favor informe o estado da cidade do(a) cliente %s: ", nomeClientes);
                    String estado = sc.nextLine();

                    enderecos = new Endereco(rua, numero, cidade, estado);

                    System.out.println("\nCliente cadastrado: " + clientes + enderecos);
                    break;

                case 2:
                    System.out.print("Caro usuário, por favor me informe quantos produtos você desejará encomendar: ");
                    int quantidadeProdutos = sc.nextInt();
                    for (int i = 0; i < quantidadeProdutos; i++) {
                        System.out.printf("\nCaro usuário, por favor informe o id do seu %do produto: ", i + 1);
                        Integer idProduto = sc.nextInt();
                        sc.nextLine();
                        System.out.printf("\nCaro usuário, por favor informe o nome do seu %do produto: ", i + 1);
                        String nomeProduto = sc.nextLine();
                        System.out.printf("\nCaro usuário, por favor informe o preço do produto %s: ", nomeProduto);
                        double precoProduto = sc.nextDouble();
                        Produto produtos = new Produto(idProduto, nomeProduto, precoProduto);
                        list.add(produtos);
                    }
                    System.out.print("\nCaro usuário, por favor insira qual sera o id do seu pedido: ");
                    Integer idPedido = sc.nextInt();
                    List<Produto> produtos = list;
                    Cliente clientePedido = clienteCadastrado;
                    Endereco enderecoPedido = enderecos;
                    statusPedido = EM_ANDAMENTO;
                    Pedido pedidos = new Pedido(idPedido, clientePedido, produtos, enderecoPedido, statusPedido);
                    pedidosGerais.add(pedidos);


                    break;

                case 3:
                    System.out.print("Caro usuário, por favor informe o id de seu pedido: ");
                    Integer idVerificação = sc.nextInt();
                    System.out.print("\nCaro usuário, seu pedido de id" + idVerificação + ", é composto por:" + pedidosGerais.stream().filter(p -> p.getId().equals(idVerificação)).findFirst().orElse(null));

                    break;

                case 4:
                    System.out.print("\nCaro usuário, seu pedido de status EM_ANDAMENTO é composto por:" + pedidosGerais.stream().filter(s -> s.getStatus() == EM_ANDAMENTO).toList());
                case 5:
                    System.out.println("Encerrando...");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }
        }

        sc.close();
    }
}
