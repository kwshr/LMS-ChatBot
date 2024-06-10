package com.example.Controllers;




import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;

import org.springframework.web.bind.annotation.RestController;

import com.example.service.modelApiService;

import com.example.model.ChatRequest;





@RestController
@CrossOrigin(origins = "http://localhost:3000/")
@RequestMapping("/spring")
public class ChatController {
    
    @Autowired
    private modelApiService modelApiService;
    
    
    
    @GetMapping("/")
	public String searchProducts(){
	    return "HEllo";
	}
    

    @PostMapping("/chat")
    public ResponseEntity<String> chatWithBot(@RequestBody ChatRequest request) {
        // Call Python Flask backend
        String response = modelApiService.getResponseFromPython(request.getInput());
        return ResponseEntity.ok(response);
    }
}
