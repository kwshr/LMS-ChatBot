

package com.example.service;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

//Annotation to indicate that this class is a service component in Spring, which is used for business logic.

@Service
public class PythonApiService {

   
    @Value("${python.backend.url}") // Injects the value of python.backend.url from application.properties
    private String pythonBackendUrl;

    private final RestTemplate restTemplate;

    public PythonApiService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // Method to communicate with Python backend and get response
    public String getResponseFromPython(String input) {
        // Constructing the URL for Python backend endpoint
        String pythonEndpoint = pythonBackendUrl + "/generate?prompt=" + input;
        
        // Making a GET request to Python backend
        ResponseEntity<String> responseEntity = restTemplate.getForEntity(pythonEndpoint, String.class);
        
        // Returning the response body
        return responseEntity.getBody();
    }
}
   