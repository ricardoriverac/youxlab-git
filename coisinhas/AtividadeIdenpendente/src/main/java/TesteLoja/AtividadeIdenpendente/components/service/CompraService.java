package TesteLoja.AtividadeIdenpendente.components.service;

import TesteLoja.AtividadeIdenpendente.components.Repositories.CompraRepository;
import TesteLoja.AtividadeIdenpendente.components.entities.Compra;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class CompraService {

    @Autowired
    private CompraRepository compraRepository;

    @Autowired
    private Compra compra;

    public Compra findCompra(Long id){
        Optional<Compra> compra = this.compraRepository.findById(id);
        return compra.orElseThrow(() -> new RuntimeException("COMPRA NÃO ENCONTRADA"));
    }


}
