const express = require('express');
const db = require('pg-promise')();
const app = express();
const PORT = process.env.PORT || 3000;

// Connect to PostgreSQL database
const connection = db({
  host: 'localhost',  // Or wherever your DB is hosted
  port: 5432,         // Default PostgreSQL port
  database: 'booking_platform',
  user: 'your_user',  // Replace with your PostgreSQL user
  password: 'your_password'  // Replace with your password
});

// Middleware to parse JSON data
app.use(express.json());

// Route to get all services
app.get('/services', async (req, res) => {
  try {
    const services = await connection.any('SELECT * FROM Services');
    res.json(services);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Route to get availability
app.get('/availability', async (req, res) => {
  try {
    const availability = await connection.any('SELECT * FROM Availability');
    res.json(availability);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Example route to create an appointment
app.post('/appointments', async (req, res) => {
  const { user_id, service_id, appointment_time } = req.body;
  try {
    const newAppointment = await connection.one(
      'INSERT INTO Appointments(user_id, service_id, appointment_time, status) VALUES($1, $2, $3, $4) RETURNING *',
      [user_id, service_id, appointment_time, 'pending']
    );
    res.json(newAppointment);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
