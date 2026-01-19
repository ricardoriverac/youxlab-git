package curso_completo_java.sessao_16.pratica.exemplo_pratica02.devices;


public class ConcreteScanner extends Device implements Scanner {

        public ConcreteScanner(String serialNumber) {
            super(serialNumber);
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

