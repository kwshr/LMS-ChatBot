import config from '../Dependencies/config.js';
import MessageParser from '../Dependencies/MessageParser.jsx';
import ActionProvider from '../Dependencies/ActionProvider.jsx';
import Chatbot from 'react-chatbot-kit';
import "./botMain.css"

const BotMain = () =>{
    return(
        <>
        <Chatbot config={config}
        messageParser={MessageParser}
        actionProvider={ActionProvider}/>
        </>
    )
}

export default BotMain;