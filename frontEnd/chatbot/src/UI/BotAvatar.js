import React from "react";
import "./BotAvatar.css"
import BotAvatar from "../Icons/BotAvatar.svg";

const ChatbotAvatar = () =>{
    return (
        <div className="react-chatbot-kit-chat-bot-avatar">
            <div className="react-chatbot-kit-chat-bot-avatar-container" style={{ background: "none" }}>
                <img className = "BotAvatar" src={BotAvatar} />
            </div>
        </div>
    )
}

export default ChatbotAvatar;