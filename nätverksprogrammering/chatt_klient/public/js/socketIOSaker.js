var socket = io();
let userName = "";
var eventEmitter = io();
let currentTypingUser = "";
let currentTypingTimeout = null;

let typingTimeout;

const message = function () {
  const input = document.querySelector(".inputField");
  let msg = input.value;
  input.value = "";
  eventEmitter.emit("message", { userName: userName, msg: msg });
};

document
  .getElementById("message-input")
  .addEventListener("keypress", function (e) {
    socket.emit("typing", userName);
  });

socket.on("message", function (msgData) {
  var element;
  if (msgData.msg.match(/\.(jpeg|jpg|gif|png)$/) != null) {
    element = document.createElement("img");
    element.src = msgData.msg;
    element.classList.add("message");
    element.alt = `${msgData.userName}'s image`;
    let p = document.createElement("p");
    p.textContent = msgData.userName + ": ";
    document.getElementById("messages").appendChild(p);
  } else {
    element = document.createElement("p");
    element.classList.add("message");
    element.textContent = `${msgData.userName}: ${msgData.msg}`;
  }
  document.getElementById("messages").appendChild(element);
});

socket.on("userExists", function (data) {
  document.getElementById("error-container").innerHTML = data;
  document.getElementById("username").style.display = "block";
});

socket.on("userSet", function (data) {
  document.getElementById("current-username").innerText =
    "Your username is: " + data.userName;
  document.getElementById("message-input").classList.remove("hidden");
  userName = data.userName;
});

socket.on("user-is-typing", function (data) {
  document.getElementById("user-typing-text").innerText =
    data + " is typing...";
  clearTimeout(typingTimeout);
  typingTimeout = setTimeout(function () {
    document.getElementById("user-typing-text").innerText = "";
  }, 2000);
});

function setUserName() {
  userName = document.getElementById("user").value;
  socket.emit("setUsername", userName);
  //hide the username input form

  document.getElementById("username").style.display = "none";
}
