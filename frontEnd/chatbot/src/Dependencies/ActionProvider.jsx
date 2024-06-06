import React from 'react';

//Responsible for handling actions triggered by the MessageParser.

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleHello = () => {
    const botMesaage = createChatBotMessage('Hello. Great to have you here :)');

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMesaage],
    }));
  };

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