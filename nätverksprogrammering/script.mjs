import express from "express";
import fs from "fs";
import url from "url";
import { Socket } from "socket.io";

const __filename = url.fileURLToPath(import.meta.url);
const __dirname = url.fileURLToPath(new URL(".", import.meta.url));

const app = express();

const port = 3000;
app.get("/", (req, res) => {
  res.sendFile(__dirname + "index.html");
});

app.get("/about", (req, res) => {
  res.send("About");
});

app.get("/time", (req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });
  res.write("the date and time are currently: " + Date());
  res.end();
});

app.listen(port, () => {
  console.log("Example app listening on port 3000!");
});

app.get("/counter", (req, res) => {
  fs.readFile("counter.txt", function (err, data) {
    var nbr = Number(data.toString());
    nbr++;
    fs.writeFile("counter.txt", nbr.toString(), function (err) {
      if (err) throw err;
    });
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.end(`Denna sida har laddats ${nbr} gånger`);
  });
});
app.use(express.urlencoded());

app.get("/skript", (req, res) => {
  res.sendFile(__dirname + "/post.html");
  var q = url.parse(req.url, true).query;
  let txt = q.year + " " + q.month;
});

app.post("/skript", (req, res) => {
  let txt = "Du skrev " + req.body.year + " " + req.body.month;
  res.send(txt);
});
