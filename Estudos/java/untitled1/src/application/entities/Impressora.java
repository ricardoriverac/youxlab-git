package application.entities;

public class Impressora extends Dispositivo {
    public Impressora(String numeroSerie) {
        super(numeroSerie);
    }

    @Override
    public void processDoc(String doc) {
        System.out.println("Processando impressora: " + doc);
    }
    public void imprimir(String doc){
        System.out.println("Imprimindo " + doc);
    }
}
