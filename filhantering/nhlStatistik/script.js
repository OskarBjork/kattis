// import promises
const { readFile, appendFile, writeFile } = require("fs/promises");

async function readThisFile(data) {
  try {
    const data = await readFile("./dummytext.txt");
    console.log(data.toString());
  } catch (error) {
    console.error(`Got an error trying to read the file: ${error.message}`);
  }
}

async function appendToFile(fileName, text) {
  try {
    await appendFile(fileName, text, { flag: "a" });
  } catch (error) {
    console.error(`Got an error trying to append to a file: ${error.message}`);
  }
}

async function writeToFile(fileName, text) {
  try {
    await writeFile(fileName, text);
    console.log(`Wrote to ${fileName}`);
  } catch (error) {
    console.error(`Got an error trying to write to a file: ${error.message}`);
  }
}

// readThisFile("./dummytext.txt");
appendToFile("./dummytext.txt", "This is a new line of text\n");
// writeToFile("./dummytext.txt", "hello");
