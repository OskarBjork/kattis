// Define the regular expression
let regex = /^[A-Z]{3}$/;

// Test the regular expression
let testString = "BOS";
let match = testString.match(regex);

if (match) {
  console.log("Match found!");
} else {
  console.log("No match found.");
}
