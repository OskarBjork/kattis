import express from "express";

const app = express();

const port = 3000;
app.get("/", (req, res) => {
  res.sendFile(
    "C:\\Users\\Elev\\Desktop\\VSCode\\Python\\programmering 2\\nätverksprogrammering\\index.html"
  );
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
