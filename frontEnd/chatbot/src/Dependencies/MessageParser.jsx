import React from 'react';

/* responsible for parsing user messages and deciding which action
* to trigger based on certain rules
*/

const MessageParser = ({ children, actions }) => {
  const greetings = ['hello','hi','hey',]
  const parse = (message) => {
    if(greetings.some(greetings => message.toLowerCase().includes(greetings)))
    actions.handleHello();
  else{
    actions.handleDefault();
    // actions.handlePrompt(message);
  }
    }

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions,
        });
      })}
    </div>
  )
};

export default MessageParser;