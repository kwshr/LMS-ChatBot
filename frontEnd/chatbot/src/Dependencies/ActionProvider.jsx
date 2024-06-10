import React, { useEffect } from 'react';

//Responsible for handling actions triggered by the MessageParser.

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleHello = () => {
    const botMesaage = createChatBotMessage('How can i help you :)');

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMesaage],
    }));
  };

  useEffect(() =>{
  const handlePrompt = async (message) =>{
    try{
      const response = await axios.get('http://localhost:5000/generate')
    } catch(error){
      console.error('Error gettign the response', error)
    }
  }
  })

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleHello,
          },
        });
      })}
    </div>
  );
};

export default ActionProvider;