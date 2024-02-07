const message = function () {
  var eventEmitter = io();
  const input = document.querySelector(".inputField");
  let msg = input.value;
  eventEmitter.emit("message", { userName: userName, msg: msg });
};

let userName = "";
var socket = io();
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
  document.getElementById("message-input").value = "";
});

socket.on("userExists", function (data) {
  document.getElementById("error-container").innerHTML = data;
  document.getElementById("username").style.display = "block";
});

socket.on("userSet", function (data) {
  // console.log("hello");
  document.getElementById("current-username").innerText =
    "Your username is: " + data.userName;
  console.log("hello");
  document.getElementById("message-input").classList.remove("hidden");
  userName = data.userName;
});

function setUserName() {
  userName = document.getElementById("user").value;
  socket.emit("setUsername", userName);
  //hide the username input form

  document.getElementById("username").style.display = "none";
}
