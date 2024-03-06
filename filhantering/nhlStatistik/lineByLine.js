// Importing the Required Modules
const fs = require("fs");
const readline = require("readline");

// Creating a readable stream from file
// readline module reads line by line
// but from a readable stream only.
const file = readline.createInterface({
  input: fs.createReadStream("teams.csv"),
  output: process.stdout,
  terminal: false,
});

const teams = {};
let counter = 0;
let text = "";
// Printing the content of file line by
// line to console by listening on the
// line event which will triggered
// whenever a new line is read from
// the stream
file.on("line", (line) => {
  text += line + "\n";
});

file.on("close", () => {
  text = text.split("\n");
  // console.log(text);
  let regex = /^[A-Z]{3}$/;

  for (let i = 0; i < text.length; i++) {
    let teamInfo = text[i].split(",");
    if (teamInfo.includes("all")) {
      let teamName = teamInfo[0];
      let goalsFor = teamInfo[12];
      teams[teamName] = goalsFor;
    }
  }
  let maxTeam = "";
  let maxScore = 0;

  for (const team in teams) {
    if (Object.hasOwnProperty.call(teams, team)) {
      const score = teams[team];
      if (score > maxScore) {
        maxScore = score;
        maxTeam = team;
      }
    }
  }
  console.log(maxTeam, maxScore);
});
