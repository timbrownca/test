import React from "react";
import "./App.css";

const postIt = () => {
  fetch("/chat_history", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
};
function App() {
  return (
    <>
      <div className="App-header">
        <h5>i-Knowledge Chatbot</h5>
      </div>
      <div className="App">Hello, world</div>
      <button onClick={() => postIt()}>click me</button>
    </>
  );
}

export default App;
