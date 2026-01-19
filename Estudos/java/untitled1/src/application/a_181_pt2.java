package application;

import application.entities.*;

public class a_181_pt2 {
    public static void main(String[] args) {
       ImpressoraConcreto p = new ImpressoraConcreto("1080");
       p.processDoc("Minha carta");
       p.imprimir("Minha carta");
        System.out.println();

        ScannerConcreto s = new ScannerConcreto("2003");
        s.processDoc("Meu email");
        System.out.println("Resultado do Scanner " + s.scan());

        System.out.println();
        ComboDispositivo c = new ComboDispositivo("2081");
        c.processDoc("minha dissertação");
        c.imprimir("Minha dissertação");
        System.out.println("Resultado do scanner: " + c.scan());

    }
}
