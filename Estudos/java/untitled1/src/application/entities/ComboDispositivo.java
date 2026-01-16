package application.entities;

public class ComboDispositivo extends Dispositivo implements Scanner, Impressora {
    public ComboDispositivo(String numeroSerie) {
        super(numeroSerie);
    }

    @Override
    public void imprimir(String doc) {
        System.out.println("Impressão combinada: " + doc);
    }

    @Override
    public String scan() {
        return "Resultado do scan combinado";
    }

    @Override
    public void processDoc(String doc) {
        System.out.println("Processando combinação: " + doc);
    }
}
