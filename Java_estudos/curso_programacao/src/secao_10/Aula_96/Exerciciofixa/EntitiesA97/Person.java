package secao_10.Aula_96.Exerciciofixa.EntitiesA97;

public class Person {
    private String name;
    private int age;
    private double height;


    public Person(String name, int age, double height){
        this.name = name;
        this.age = age;
        this.height = height;
    }

    public Person(){

    }


    public String getName(){
        return this.name;
    }


    public void setName(String name){
        if (name.length() < 3){
            System.out.println("Nome precisa ser maior que 3 caracteres");
        }else{
            this.name = name;
        }
    }


    public int getAge(){
        return this.age;
    }


    public void setAge(int age){
        this.age = age;
    }



    public double getHeight() {
        return height;
    }


    public void setHeight(double height) {
        this.height = height;
    }

    public String toString(){
        return "Name: " + name
                + "\nAge: " + age
                + "\nHeight: " + height;
    }


}
