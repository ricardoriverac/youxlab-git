package com.example.security;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfig {


    @Autowired
    private SecurityFilter securityFilter;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        return http
                .csrf(csrf -> csrf.disable())
                .sessionManagement(sm -> sm.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .authorizeHttpRequests(req -> {

                    req.requestMatchers(HttpMethod.POST, "/admin/criar-admin").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/admin/users").permitAll();
                    req.requestMatchers(HttpMethod.PUT, "/admin/user/{id}/bloquear").permitAll();
                    req.requestMatchers(HttpMethod.PUT, "/admin/user/{id}/desbloquear").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/admin/user/bloqueados").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/admin/user/pendentes").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/admin/listar-todos").permitAll();
                    req.requestMatchers(HttpMethod.DELETE, "/admin/user/{id}/deletar").permitAll();

                    req.requestMatchers(HttpMethod.POST, "/auth/login").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/auth/confirmar-email").permitAll();
                    req.requestMatchers(HttpMethod.POST, "/auth/esqueci-senha").permitAll();
                    req.requestMatchers(HttpMethod.POST, "/auth/resetar-senha").permitAll();

                    req.requestMatchers(HttpMethod.GET, "/dashboard/dashboard-todos").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/dashboard/admin").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/dashboard/user/{userId}").permitAll();

                    req.requestMatchers(HttpMethod.POST, "/jogo/iniciar").permitAll();
                    req.requestMatchers(HttpMethod.POST, "/jogo/jogar").permitAll();
                    req.requestMatchers(HttpMethod.POST, "/jogo/encerrar/{jogoId}").permitAll();
                    req.requestMatchers(HttpMethod.GET, "/jogo/atual/{userId}").permitAll();

                    req.requestMatchers(HttpMethod.POST, "/user/cadastro").permitAll();
                    req.requestMatchers(HttpMethod.PUT, "/user/atulizar/{id}").permitAll();



                    req.requestMatchers("/admin/**").hasRole("ADMIN");
                    req.requestMatchers("/user/**").authenticated();

                    req.anyRequest().authenticated();
                })
                .addFilterBefore(securityFilter, UsernamePasswordAuthenticationFilter.class)
                .build();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    }

