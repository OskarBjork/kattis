import express from "express";
import { createServer } from "http";
import { Server } from "socket.io";

const app = express();
const server = createServer(app);
const io = new Server(server);

// Global variables

const triviaQuestions = {
  question1: {
    question: "What is the capital of France?",
    answer: "Paris",
  },
  question2: {
    question: "What is the capital of Germany?",
    answer: "Berlin",
  },
  question3: {
    question: "What is the capital of Spain?",
    answer: "Madrid",
  },
};

const questionKeys = Object.keys(triviaQuestions);

let currentQuestionAnswer = null;

// Functions

function getRandomQuestionKey() {
  const randomIndex = Math.floor(Math.random() * questionKeys.length);
  return triviaQuestions[questionKeys[randomIndex]];
}

function sendQuestionToSocket(socket) {
  const randomQuestion = getRandomQuestionKey();
  currentQuestionAnswer = randomQuestion.answer;
  socket.emit("question", randomQuestion.question);
}

app.use(express.static("public"));

// IO events

io.on("connection", (socket) => {
  console.log("A user connected");
  sendQuestionToSocket(socket);

  socket.on("answer", (data) => {
    console.log("Answer received:", data);
  });
});

server.listen(3000, () => {
  console.log("Server is running on port 3000");
});
