package sistema_pedidos_POO.application;

import sistema_pedidos_POO.etities.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class program {

    private static StatusPedido lerStatus() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print(
                    "Digite o status: \n" +
                            "1 → AGUARDANDO_ENVIO\n" +
                            " 2 →  EM_ANDAMENTO\n" +
                            " 3 →  ATRASADO\n" +
                            " 4 →  ENTREGUE\n"
            );
            int statusDigitado = scanner.nextInt();

            switch (statusDigitado) {
                case 1:
                    return StatusPedido.AGUARDANDO_ENVIO;

                case 2:
                    return StatusPedido.EM_ANDAMENTO;

                case 3:
                    return StatusPedido.ATRASADO;

                case 4:
                    return StatusPedido.ENTREGUE;

                default:
                    System.out.println("Opção inválida! Digite um número das opções: ");
                    break;
            }

        }

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        List<Cliente> clientes = List.of(
                new Cliente(1, "Livia", "livia@email.com"),
                new Cliente(2, "Carla", "carla@email.com"),
                new Cliente(3, "Carlos", "carlos@email.com"),
                new Cliente(4, "Fernanda", "fer@email.com"),
                new Cliente(5, "Eduardo", "edu@email.com")
        );

        List<Produto> produtos = List.of(
                new Produto(1, "Garrafa", 50.0),
                new Produto(2, "Notebook", 3000.0),
                new Produto(3, "Celular", 4000.0),
                new Produto(4, "Tapete", 30.0),
                new Produto(5, "Mouse", 70.0),
                new Produto(6, "Fone", 15.0)
        );

        List<Pedido> pedidos = new ArrayList<>(
        );

        pedidos.add(new Pedido(
                8,
                clientes.get(4),
                new Endereco("João Silva", "42", "Mato Grosso", "BH"),
                StatusPedido.AGUARDANDO_ENVIO,
                Arrays.asList(
                        produtos.get(1),
                        produtos.get(5)
        )));


        pedidos.add(new Pedido(
                6,
                clientes.get(1),
                new Endereco("Carmen", "34", "Filipinas", "RJ"),
                StatusPedido.ATRASADO,
                Arrays.asList(
                        produtos.get(4),
                        produtos.get(3)
                )
        ));

        int opcao = -1;

        while (opcao != 0) {

            System.out.println("\n→ MENU ←");
            System.out.println("1 → Buscar pedido por id");
            System.out.println("2 → Ver valor total do pedido");
            System.out.println("3 → Buscar pedidos por status");
            System.out.println("0 → Sair");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();

            switch (opcao) {

                case 1:
                    System.out.print("Digite o id do pedido: ");
                    int buscaID = scanner.nextInt();

                    boolean resultadoID = false;
                    for (Pedido pedido : pedidos) {
                        if (pedido.getId() == buscaID) {
                            System.out.println(pedido);
                            resultadoID = true;
                            break;
                        }
                    }

                    if (!resultadoID) {
                        System.out.println("Pedido não encontrado");
                    }
                    break;

                case 2:
                    System.out.print("Digite o id do pedido: ");
                    int idTotal = scanner.nextInt();

                    boolean encontrado = false;
                    for (Pedido pedido : pedidos) {
                        if (pedido.getId() == idTotal) {
                            System.out.println(" O valor total é: R$ " + pedido.valorTotal());
                            encontrado = true;
                            break;
                        }
                    }

                    if (!encontrado) {
                        System.out.println("Pedido não encontrado.");
                    }
                    break;

                case 3:
                     StatusPedido status = lerStatus();

                    boolean existente = false;
                    for (Pedido pedido : pedidos) {
                        if (pedido.getStatus() == status) {
                            System.out.println(pedido);
                            existente = true;
                        }
                    }

                    if (!existente) {
                        System.out.println("Nenhum pedido com esse status");
                    }
                    break;

                case 0:
                    System.out.println("→ Encerrado ←");
                    break;

                default:
                    System.out.println("Digite outra opção!");
            }
        }

        scanner.close();
    }






}
