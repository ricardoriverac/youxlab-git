package application;

import application.entities.AluguelCarro;
import application.entities.ImpostoBrasilServico;
import application.entities.ServicoAluguel;
import application.entities.Veiculo;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class a_174_ex {
    public static void main(String[] args) throws ParseException {
                Locale.setDefault(Locale.US);
                Scanner sc = new Scanner(System.in);
                SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm");

                System.out.print("Caro usuário, por favor insira o modelo do carro: ");
                String modeloCarro = sc.next();
                System.out.print("Caro usuário, por favor escolha a data do aluguel: (dd/MM/yyyy HH:mm)");
                Date inicio = sdf.parse(sc.nextLine());
                System.out.print("Caro usuário, por favor escolha a data de retorno: (dd/MM/yyyy HH:mm");
                Date fim = sdf.parse(sc.nextLine());

                AluguelCarro ac = new AluguelCarro(inicio, fim, new Veiculo(modeloCarro));

                System.out.print("Caro usuário, por favor escolha o preço do aluguel por hora: ");
                Double precoHora = sc.nextDouble();
                System.out.print("Caro usuário, por favor escolha o preço do aluguel por dia: ");
                Double precoDia = sc.nextDouble();

                ServicoAluguel servicoAluguel = new ServicoAluguel(precoDia, precoHora, new ImpostoBrasilServico());
                servicoAluguel.processoFatura(ac);
                System.out.print("FATURA: ");
                System.out.print("Pagamento basico: " + String.format("%.2f", ac.getFatura().getPagamentoBasico()));
                System.out.print("Imposto: " + String.format("%.2f", ac.getFatura().getPagamentoBasico()));
                System.out.print("Pagamento total: " + String.format("%.2f", ac.getFatura().getPaymentTotal()));
                sc.close();
            }
        }
