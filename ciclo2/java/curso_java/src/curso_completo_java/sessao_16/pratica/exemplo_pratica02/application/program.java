package curso_completo_java.sessao_16.pratica.exemplo_pratica02.application;

// AULA 181 - Herança múltipla eo o problema do diamante

import curso_completo_java.sessao_16.pratica.exemplo_pratica02.devices.ComboDevice;
import curso_completo_java.sessao_16.pratica.exemplo_pratica02.devices.ConcretePrinter;
import curso_completo_java.sessao_16.pratica.exemplo_pratica02.devices.ConcreteScanner;

public class program {

    public static void main(String[] args) {

        ConcretePrinter p = new ConcretePrinter("1080");
        p.processDoc("My Letter");
        p.print("My Letter");

        System.out.println();
        ConcreteScanner s = new ConcreteScanner("2003");
        s.processDoc("My Email");
        System.out.println("Scan result: " + s.scan());

        System.out.println();
        ComboDevice c = new ComboDevice("2081");
        c.processDoc("My dissertation");
        c.print("My dissertation");
        System.out.println("Scan result: " + c.scan());
    }
}

