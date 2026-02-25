package com.api.parking_control.controllers;

import com.api.parking_control.dtos.ParkingSpotDto;
import com.api.parking_control.models.ParkingSpotModel;
import com.api.parking_control.services.ParkingSpotService;
import org.springframework.beans.BeanUtils;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.HashMap;
import java.util.Map;

@RestController
@CrossOrigin(origins = "*", maxAge = 3600)
@RequestMapping("/parking-spot")
public class ParkingSpotController {

    final ParkingSpotService parkingSpotService;

    public ParkingSpotController(ParkingSpotService parkingSpotService) {
        this.parkingSpotService = parkingSpotService;
    }

    @PostMapping
    public ResponseEntity<Object> saveParkingSpot(@RequestBody @Valid ParkingSpotDto parkingSpotDto) {

        // LOG 1: Verificar se o método foi chamado
        System.out.println(">>> MÉTODO saveParkingSpot FOI CHAMADO!");

        // LOG 2: Verificar os dados recebidos
        System.out.println(">>> DADOS RECEBIDOS:");
        System.out.println("parkingSpotNumber: " + parkingSpotDto.getParkingSpotNumber());
        System.out.println("licensePlateCar: " + parkingSpotDto.getLicensePlateCar());
        System.out.println("brandCar: " + parkingSpotDto.getBrandCar());
        System.out.println("modelCar: " + parkingSpotDto.getModelCar());
        System.out.println("colorCar: " + parkingSpotDto.getColorCar());
        System.out.println("responsibleName: " + parkingSpotDto.getResponsibleName());
        System.out.println("apartment: " + parkingSpotDto.getApartment());
        System.out.println("block: " + parkingSpotDto.getBlock());

        try {
            var parkingSpotModel = new ParkingSpotModel();
            BeanUtils.copyProperties(parkingSpotDto, parkingSpotModel);
            parkingSpotModel.setRegistrationDate(LocalDateTime.now(ZoneId.of("UTC")));

            // LOG 3: Confirmar que vai salvar
            System.out.println(">>> SALVANDO NO BANCO...");

            var savedSpot = parkingSpotService.save(parkingSpotModel);

            // LOG 4: Sucesso
            System.out.println(">>> SALVO COM SUCESSO! ID: " + savedSpot.getId());

            return ResponseEntity.status(HttpStatus.CREATED).body(savedSpot);

        } catch (Exception e) {
            // LOG 5: Erro
            System.out.println(">>> ERRO AO SALVAR: " + e.getMessage());
            e.printStackTrace();

            Map<String, String> error = new HashMap<>();
            error.put("error", e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
        }
    }
}