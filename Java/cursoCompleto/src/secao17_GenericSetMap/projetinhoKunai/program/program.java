package secao17_GenericSetMap.projetinhoKunai.program;

import secao17_GenericSetMap.projetinhoKunai.mets.BolsaNinja;
import secao17_GenericSetMap.projetinhoKunai.mets.Kunai;
import secao17_GenericSetMap.projetinhoKunai.mets.Pergaminhos;
import secao17_GenericSetMap.projetinhoKunai.mets.Shurikens;

public class program {
    public static void main(String[] args) {
        BolsaNinja<Object> bolsaNinja = new BolsaNinja<>();
        bolsaNinja.adicionarFerramenta(new Kunai("Explosivo"));
        bolsaNinja.adicionarFerramenta(new Shurikens(3));
        bolsaNinja.adicionarFerramenta(new Pergaminhos("Veneno"));
        bolsaNinja.mostrarFerramenta();
    }

}
