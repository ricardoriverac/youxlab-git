package TesteLoja.AtividadeIdenpendente.components.Repositories;

import TesteLoja.AtividadeIdenpendente.components.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
