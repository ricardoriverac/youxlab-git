
package com.casaaposta.repository;

import com.casaaposta.model.Game;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.UUID;

public interface GameRepository extends JpaRepository<Game, UUID> {
}
