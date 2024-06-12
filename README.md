# LMS-ChatBot

## Overview
This project is a chatbot built using a GPT-based model. The LLM/ directory uses code from the book "Build A Large Language Model (From Scratch)" by Sebastian Raschka.

## Credits
This project includes code from "Build A Large Language Model (From Scratch)" by Sebastian Raschka.

If you find this book or code useful for your research, please consider citing it:

```
@book{build-llms-from-scratch-book,
  author       = {Sebastian Raschka},
  title        = {Build A Large Language Model (From Scratch)},
  publisher    = {Manning},
  year         = {2023},
  isbn         = {978-1633437166},
  url          = {https://www.manning.com/books/build-a-large-language-model-from-scratch},
  note         = {Work in progress},
  github       = {https://github.com/rasbt/LLMs-from-scratch}
}

```
## Setup Instructions

### - To set up the pre-trained model and generate responses, follow these steps:

1. Clone the Repository:
    ```bash
    git clone https://github.com/kwshr/LMS-ChatBot.git
    cd LMS-ChatBot
    ```

2. Navigate to the LLM Directory:
    ```bash
    cd LLM
    ```

3. Run the Main Script:
    ```bash
    python main.py
    ```
    The script will prompt you to enter a prompt and the maximum number of tokens to generate. 

4. Optional Configuration:
    - If you want to manually edit the `top-k` and `temperature` settings to generate more coherent texts, you can do so by editing the `main.py` file:
      
        ```bash
        # Open main.py
        nano main.py

        # Locate the configuration section and adjust the parameters as needed
        top_k = <desired_value>  # Example: top_k = 40
        temperature = <desired_value>  # Example: temperature = 0.7
        ```

### - To set up the backend part of the project, follow these steps:


1. Clone the Repository:
    ```bash
    git clone https://github.com/kwshr/LMS-ChatBot.git
    cd LMS-ChatBot
    ```

2. Navigate to the LLM Directory:
    ```bash
    cd backend/Chatbot
    ```

3. Since application relies on a pre-trained model hosted on a separate Python Flask backend, ensure it is up and running. Follow the instructions provided for the Python backend setup.     

4. Configure Application Properties
Before running the application, configure the necessary properties in application.properties located in src/main/resources.

5. Run the Main Script:
    ```bash
    mvn clean install
    mvn spring-boot:run
    ```

Your application backend is now set up and running. 

       

### - To set up the frontend part of the project, follow these steps:






