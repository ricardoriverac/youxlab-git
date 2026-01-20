package secao_16.aula_181.devices;

public class ConcreteScanner extends Device implements Scanner {

    public ConcreteScanner(String serialNumber) {
        super(serialNumber);
    }

    @Override
    public void print(String doc) {
    }

    @Override
    public void processDoc(String doc) {
        System.out.println("Scanner processing: " + doc);
    }

    @Override
    public String scan() {
        return "Scanned content";
    }
}