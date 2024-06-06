import logo from './logo.svg';
import './App.css';
import Chatbot from 'react-chatbot-kit';
import 'react-chatbot-kit/build/main.css';
import BotMain from './bot/botMain';

function App() {
  return (
    <>
     <div className='chatbotInterface'>
      <BotMain/>
     </div>
    </>
  );
}

export default App;
