package com.example.repository;

public interface UserRepository extends JpaRepository<User, Long>{
    Optional<User> findByEmail(String email);
    Optional<User> findByTokenConfirmacao(String token);
    boolean existsByEmail(String email);
}
