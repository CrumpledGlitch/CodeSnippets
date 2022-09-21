// This script takes user input and generates a QR code that is displayed in the terminal.
// The QR code is generated using the qrcode-terminal module.
// The user input is taken using the readline-sync module.
// The user input is then passed to the qrcode-terminal module to generate the QR code.
// The QR code is then displayed in the terminal.

// Importing the readline-sync module
const readline = require('readline-sync');

// Importing the qrcode-terminal module
const qrcode = require('qrcode-terminal');

// Taking user input
const input = readline.question('Enter the text to be converted to QR code: ');

// Generating the QR code
qrcode.generate(input);

// Displaying the QR code in the terminal
qrcode.generate(input, {small: true});

