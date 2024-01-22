import express from "express";
import http from "http";
import url from "url";
import * as socketIO from "socket.io";

const __filename = url.fileURLToPath(import.meta.url);
const __dirname = url.fileURLToPath(new URL(".", import.meta.url));

const app = express();
const server = http.createServer(app);
const io = new socketIO.Server(server);

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/klient.html");
});
io.on("connection", function (socket) {
  socket.on("scream", function (data) {
    console.log("I heard a scream: " + data);
  });
});
server.listen(8080, function () {
  console.log("listening on *:8080");
});
