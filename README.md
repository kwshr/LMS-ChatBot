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
    python PreTrainMain.py
    ```
    The script will prompt you to enter a prompt and the maximum number of tokens to generate. 

4. Optional Configuration:
    - If you want to manually edit the `top-k` and `temperature` settings to generate more coherent texts, you can do so by editing the `PreTrainMain.py` file:
      
        ```bash
        # Open PreTrainMain.py
        nano PreTrainMain.py

        # Locate the configuration section and adjust the parameters as needed
        top_k = <desired_value>  # Example: top_k = 40
        temperature = <desired_value>  # Example: temperature = 0.7
        ```
       

### - To set up the frontend part of the project, follow these steps:

1. Navigate to the Frontend Directory:
    ```bash
    cd frontEnd/chatbot
    ```

2. Install Dependencies:
    ```bash
    npm install
    ```

    This command will install all the required packages listed in the `package.json` file.

3. Start the Development Server:
    ```bash
    npm start
    ```

    The application should now be running on `http://localhost:3000/`, and you can interact with the chatbot through the web interface.

4. Build for Production (Optional):
    ```bash
    npm run build
    ```

    This command will create an optimized build of the app, ready for deployment.



