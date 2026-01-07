package secao7_introOrientacaoaObjetos.entities; //pacote da classe

// declarando a classe
public class triangle {
    public double a;
    public double b;
    public double c;
    // declarando seus atributos de classe

    public double area(/*lista de parâmetros*/)
        /*O double define o tipo de dado que o método retorna*/
    //declarando método da classe
    {
        double p = (a + b + c) / 2.0;
        return Math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ) );
    }// corpo do método
}
