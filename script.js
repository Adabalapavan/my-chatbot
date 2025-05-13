const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function addMessage(sender, text) {
  const message = document.createElement("div");
  message.classList.add("message");
  message.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const message = userInput.value.trim();
  if (message === "") return;

  addMessage("You", message);
  userInput.value = "";

  fetch("http://localhost:5005/webhooks/rest/webhook", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ sender: "user", message: message })
  })
    .then(response => response.json())
    .then(data => {
      data.forEach((res) => {
        addMessage("Bot", res.text);
      });
    })
    .catch(error => {
      console.error("Error:", error);
      addMessage("Bot", "Sorry, the server is not responding.");
    });
}
