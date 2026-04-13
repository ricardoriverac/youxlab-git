package com.example.casaDeApostas.security;

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
public class SecurityConfiguration {

    @Autowired
    private SecurityFilter filter;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity httpSecurity) {
        return httpSecurity
                .csrf(csrf -> csrf.disable())
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .authorizeHttpRequests(authorize -> authorize
                        .requestMatchers(HttpMethod.POST, "/casa-apostas/login").permitAll()
                        .requestMatchers(HttpMethod.PUT, "/casa-apostas/reset-password").hasAnyRole("ADMIN", "USER")

                        .requestMatchers(HttpMethod.POST, "/usuario/user/register-users").permitAll()

                        .requestMatchers(HttpMethod.GET, "/usuario/admins/all-users/bloquear").hasRole("ADMIN")
                        .requestMatchers(HttpMethod.GET, "/usuario/admins/all-users").hasRole("ADMIN")
                        .requestMatchers(HttpMethod.GET, "/usuario/admins/cpf/{cpf}").hasRole("ADMIN")
                        .requestMatchers(HttpMethod.POST, "/usuario/admins/register-admins").permitAll()

                        .requestMatchers(HttpMethod.POST, "/account/create-account").hasAnyRole("USER", "ADMIN")
                        .requestMatchers(HttpMethod.POST, "/account/depositar").hasAnyRole("USER", "ADMIN")


                        .requestMatchers(HttpMethod.POST, "/jogos/jogar").permitAll()
                        .requestMatchers(HttpMethod.POST, "/jogos/encerrar").hasAnyRole("USER", "ADMIN")
                        .requestMatchers(HttpMethod.POST, "/jogos/criar-jogo").hasAnyRole("USER", "ADMIN")

                        .anyRequest().authenticated()
                )
                .addFilterBefore(filter, UsernamePasswordAuthenticationFilter.class)
                .build();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration){
        return authenticationConfiguration.getAuthenticationManager();
    }

    @Bean
    public PasswordEncoder passwordEncoder(){
        return new BCryptPasswordEncoder();
    }
}