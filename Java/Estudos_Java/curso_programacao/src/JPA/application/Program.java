//package JPA.application;
//
//import JPA.dominio.Pessoa;
//
//public class Program {
//    static void main() {
//
//        Pessoa p1 = new Pessoa(null, "Carlos da Silva", "carlos@gmail.com");
//        Pessoa p2 = new Pessoa(null, "Joaquim Torres", "joaquim@gmail.com");
//        Pessoa p3 = new Pessoa(null, "Ana Maria", "ana@gmail.com");
//
//        //EntityManagerFactory emf = Persistence.createEntityManagerFactory("exemplo-jpa");
//        //EntityMaganer em = emf.createEntityManager();
//        em.getTransaction().begin();
//        em.persist(p1);
//        em.persist(p2);
//        em.persist(p3);
//        em.getTransaction().commit();
//
//        Pessoa p = em.find(Pessoa.class, 2);
//        System.out.println(p);

//        Pessoa p = em.find(Pessoa.class, 2):
//        em.getTransation().begin;
//        em.remove(p);
//        em.getTransation().commit();

 //       System.out.println("Pronto!");
//        em.close();
//        emf.close();
//    }
//}
