import { createChatBotMessage } from 'react-chatbot-kit';
import ChatbotAvatar from '../UI/BotAvatar.js';
import UserAvatarIcon from '../UI/UserAvatar.js'

const botName = 'YorkCourseWizard';

const config = {
  initialMessages: [createChatBotMessage(`Hi! I'm ${botName}`)],
  customStyles: {
    botMessageBox: {
      backgroundColor: 'red',
    },
    chatButton: {
      backgroundColor: 'red',
    },
  },

  customComponents: {
    // Replaces the default header
   header: () => <div style={{ backgroundColor: 'red', padding: "5px", borderRadius: "3px" , display: "ruby-text"}}>YorkCourseWizard</div>,
   // Replaces the default bot avatar
   botAvatar: (props) => <ChatbotAvatar {...props} />,
   // Replaces the default user icon
   userAvatar: (props) => <UserAvatarIcon {...props} />,
  //  // Replaces the default bot chat message container
  //  botChatMessage: (props) => <MyCustomChatMessage {...props} />,
  
  //  // Replaces the default user chat message
  //  userChatMessage: (props) => <MyCustomUserChatMessage {...props} />
 },

};

export default config;