import express from "express";
import http from "http";
import url from "url";
import * as socketIO from "socket.io";
import say from "say";
import fs from "fs";
import axios from "axios";

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
    const text = data; // Replace this with your story text
    const url = `https://westus.tts.speech.microsoft.com/cognitiveservices/v1`;
    const options = {
      method: "POST",
      headers: {
        "Ocp-Apim-Subscription-Key": "<Your Subscription Key>", // Replace this with your subscription key
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
        "User-Agent": "YOUR_RESOURCE_NAME",
      },
      data: `<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Female' name='en-US-JessaRUS'>${text}</voice></speak>`,
      responseType: "arraybuffer",
    };
    axios(url, options)
      .then((response) => {
        fs.writeFileSync("output.wav", response.data);
        say.speak("output.wav");
      })
      .catch((err) => console.error(err));
  });
});
server.listen(8080, function () {
  console.log("listening on *:8080");
});
