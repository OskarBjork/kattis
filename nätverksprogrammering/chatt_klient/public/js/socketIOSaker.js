const message = function () {
  var eventEmitter = io();
  const input = document.querySelector(".inputField");
  let msg = input.value;
  eventEmitter.emit("message", { userName: userName, msg: msg });
};

let userName = "";
var socket = io();
socket.on("message", function (msgData) {
  var p = document.createElement("p");
  p.textContent = `${msgData.userName}: ${msgData.msg}`;
  document.body.appendChild(p);
});

socket.on("userExists", function (data) {
  document.getElementById("error-container").innerHTML = data;
  document.getElementById("username").style.display = "block";
});

socket.on("userSet", function (data) {
  document.getElementById("current-username").innerText =
    "Your username is: " + data.userName;

  userName = data.userName;
});

function setUserName() {
  userName = document.getElementById("user").value;
  socket.emit("setUsername", userName);
  //hide the username input form

  document.getElementById("username").style.display = "none";
}
