package application.entities;

public class Scanner extends Dispositivo{

    public Scanner(String numeroSerie) {
        super(numeroSerie);
    }

    @Override
    public void processDoc(String doc){
        System.out.println("Scanner está processando: " + doc);
    }

    public String scan(){
        return "Conteúdo scanneado";
    }
}
