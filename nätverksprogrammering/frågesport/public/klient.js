// Module inits

const socket = io();

// HTML elements

const questionParagraph = document.getElementById("question-text");
const submitButton = document.getElementById("submit");

// Functions

const answer = (event) => {
  console.log("Answering question");
  event.preventDefault();
  const answerInput = document.getElementById("answer");
  const answer = answerInput.value;
  socket.emit("answer", answer);
  answerInput.value = "";
};

console.log("Klient.js");

// Socket events

socket.on("question", (data) => {
  questionParagraph.textContent = data;
});

socket.on("answerResponse", (data) => {
  console.log("Answer response received:", data);
  document.getElementById("question-response").textContent = data;
});

// Main

function main() {}
main();

// Event listeners

submitButton.addEventListener("click", answer);
