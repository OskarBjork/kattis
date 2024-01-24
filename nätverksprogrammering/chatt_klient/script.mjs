import express from "express";
import http from "http";
import url from "url";
import * as socketIO from "socket.io";
import fs from "fs";
import axios from "axios";

const __filename = url.fileURLToPath(import.meta.url);
const __dirname = url.fileURLToPath(new URL(".", import.meta.url));

const app = express();
const server = http.createServer(app);
const io = new socketIO.Server(server);

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/klient.html");
});

io.on("connection", (socket) => {
  console.log("Client connected");
  socket.on("message", (msg) => {
    console.log("Message received: " + msg);
    io.emit("message", msg);
  });
});

server.listen(3000, () => {
  console.log("Server listening on port 3000");
});
