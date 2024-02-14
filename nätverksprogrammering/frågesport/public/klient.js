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

// Socket events

socket.on("question", (data) => {
  questionParagraph.textContent = data;
});

// Main

function main() {}
main();

// Event listeners

submitButton.addEventListener("click", answer);
