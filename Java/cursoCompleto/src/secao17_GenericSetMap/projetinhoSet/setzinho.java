package secao17_GenericSetMap.projetinhoSet;

import java.util.LinkedHashSet;
import java.util.Set;

public class setzinho {
    public static void main(String[] args) {
        Set<Manga> mangas = new LinkedHashSet<>();

        mangas.add(new Manga(5, "Dragon Ball", 50.00));
        mangas.add(new Manga(3, "HUNTER X HUNTER", 50.00));
        mangas.add(new Manga(4, "Hellsing Ultimate", 50.00));

        for (Manga manga: mangas){
            System.out.println(manga);
        }
    }
}
