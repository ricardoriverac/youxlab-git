package application;

import java.io.File;

public class a_167_ex_pastas {
    public static void main(String[] args) {
//        String strCaminho = "/home/youx";
//        File pasta = new File(strCaminho + "//pastaexercicio");
//        Boolean sucess = pasta.mkdir();
//        System.out.println("DIretório criado com sucesso" + sucess);
        String strCaminho = "/home/youx//pastaexercicio";
        File subPasta = new File(strCaminho + "/out");
        Boolean sucess = subPasta.mkdirs();
        System.out.println("Diretorio criado com sucesso" + sucess);
    }
}
