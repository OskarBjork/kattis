import express from "express";
import http from "http";
import url from "url";
import * as socketIO from "socket.io";
import fs from "fs";
import axios from "axios";

const app = express();
const server = http.createServer(app);
const io = new socketIO.Server(server);

app.use(express.static("public"));

app.get("/", (req, res) => {});
let users = [];

io.on("connection", (socket) => {
  console.log("Client connected");
  socket.on("message", (msgData) => {
    // Titta på meddelandet och se vilken klient som skickade det, sedan välj rätt användarnamn
    console.log("Message received: " + msgData.msg);
    io.emit("message", { userName: msgData.userName, msg: msgData.msg });
  });

  socket.on("setUsername", (userName) => {
    console.log("Username received: " + userName);
    if (users.includes(userName)) {
      socket.emit(
        "userExists",
        userName + " username is taken! Try some other username."
      );
    } else {
      users.push(userName);
      socket.userName = userName;
      socket.emit("userSet", { userName });
      console.log("hello");
    }
  });
});

server.listen(3000, () => {
  console.log("Server listening on port 3000");
});
