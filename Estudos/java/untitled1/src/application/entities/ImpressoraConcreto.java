package application.entities;

public class ImpressoraConcreto extends Dispositivo implements Impressora {
    public ImpressoraConcreto(String numeroSerie) {
        super(numeroSerie);
    }

    @Override
    public void processDoc(String doc){
        System.out.println("Processando escaneamento: " + doc);
    }

    @Override
    public void imprimir(String doc){
        System.out.println("Imprimindo: " + doc);
    }
}
