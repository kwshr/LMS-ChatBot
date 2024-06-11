package com.example.Chatbot.controllers;





import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;

import org.springframework.web.bind.annotation.RestController;

import com.example.Chatbot.model.ChatRequest;
import com.example.Chatbot.service.modelApiService;






@RequestMapping("/spring")
@RestController
public class ChatController {
    
    @Autowired
    private modelApiService modelApiService;
    
    
    
    @GetMapping("/")
	public String searchProducts(){
	    return "Hello";
	}
    

    @PostMapping("/chat")
    public ResponseEntity<String> chatWithBot(@RequestBody ChatRequest request) {
    	
        // Call Python Flask backend
        String response = modelApiService.getResponseFromPython(request.getInput());
        
        return ResponseEntity.ok(response);
    }
}
