const { appendFile } = require("fs/promises");
const fs = require("fs");
const readLine = require("readline");

async function appendToFile(fileName, data) {
  try {
    await appendFile(fileName, data, { flag: "w" });
    console.log(`Appended data to ${fileName}`);
  } catch (error) {
    console.error(`Got an error trying to append the file: {error.message}`);
  }
}

// appendFile("./datafiler/example.txt", "Hello, world!");

function createFiles() {
  const randomNumberBetweenOneAndHundred = Math.floor(Math.random() * 100);
  for (let i = 0; i < 100; i++) {
    appendToFile(
      `./datafiler/file${i + 1}.txt`,
      `Hello, world! ${i + 1}\n` +
        `${i + 1 === randomNumberBetweenOneAndHundred ? "Bingo!" : ""}`
    );
  }
}

function searchFiles() {
  for (let i = 0; i < 100; i++) {
    const file = readLine.createInterface({
      input: fs.createReadStream(`./datafiler/file${i + 1}.txt`),
      output: process.stdout,
      terminal: false,
    });
    file.on("line", (line) => {
      if (line.includes("Bingo!")) {
        console.log(`Found in file${i + 1}.txt`);
      }
    });
  }
}
searchFiles();
