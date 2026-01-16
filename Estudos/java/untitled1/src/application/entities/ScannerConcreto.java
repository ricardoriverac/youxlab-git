package application.entities;

public class ScannerConcreto extends Dispositivo implements Scanner{
    public ScannerConcreto(String numeroSerie) {
        super(numeroSerie);
    }

    @Override
    public void processDoc(String doc){
        System.out.println("Processando scanner: " + doc);
    }

    @Override
    public String scan(){
        return "Conteúdo scanneado";
    }
}
