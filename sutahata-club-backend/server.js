const express = require('express');
const path = require('path');

const app = express();
const PORT = 8080;

// Serve static files like CSS, JS, images
app.use('/static', express.static(path.join(__dirname, 'frontend')));

// Serve index.html at "/"
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'index.html'));
});

// Serve login.html at "/login"
app.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'login.html'));
});

// Simple test API
app.get('/api/ping', (req, res) => {
  res.json({ message: 'pong' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
