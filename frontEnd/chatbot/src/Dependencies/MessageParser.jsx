import React from 'react';

/* responsible for parsing user messages and deciding which action
* to trigger based on certain rules
*/

const MessageParser = ({ children, actions }) => {
  const parse = (message) => {
    if(message.includes('hello')){
    actions.handleHello();
    }
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions,
        });
      })}
    </div>
  );
};

export default MessageParser;