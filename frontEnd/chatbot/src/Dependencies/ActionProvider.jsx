import React, { useEffect } from 'react';
import axios from 'axios';
//import { botMessage } from 'react-chatbot-kit/build/src/components/Chat/chatUtils';

//Responsible for handling actions triggered by the MessageParser.

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const setChatBotMessage = (message) =>{
    const botMessage = createChatBotMessage(message);
    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  }

  const handleHello = () => {
    setChatBotMessage('How can i help you :)');
  };

  const handleDefault = ()=>{
    setChatBotMessage('ChatBot is under development! Please, come back at a later date :)')
  }

  const handlePrompt = async (message) =>{
    try{
      const response = await axios.get('http://localhost:5000/generate',{
        params: {prompt: message}
      })
      setChatBotMessage(response.data.generated_text);
    } catch(error){
      console.error('Error gettign the response', error);
      setChatBotMessage('Sorry, there was an error processing your request');
    }
  }

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleHello,
            handlePrompt,
            handleDefault,
          },
        });
      })}
    </div>
  );
};

export default ActionProvider;