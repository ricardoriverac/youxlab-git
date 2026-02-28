package Secao16.aula181;

public class ConcretScanner extends Device implements Scanner{

    public ConcretScanner(String serialNumber) {
        super(serialNumber);
    }

    @Override
    public void processDoc(String doc){
        System.out.println("Scanner Processing: "+ doc);
    }
    @Override
    public String scan(){
        return "Scanned content";
    }
}
