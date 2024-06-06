import React from "react";
import "./UserAvatar.css"
import UserAvatar from "../Icons/UserAvatar.svg";

const UserAvatarIcon = () =>{
    return (
        <div className="react-chatbot-kit-user-avatar-icon">
            <div className="react-chatbot-kit-user-avatar-container" style={{ background: "none" }}>
                <img className = "UserAvatar" src={UserAvatar} />
            </div>
        </div>
    )
}

export default UserAvatarIcon;