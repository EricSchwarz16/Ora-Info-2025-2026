CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) CHECK (role IN ('admin', 'doctor', 'client')) NOT NULL
);

-- Insert sample users
INSERT INTO Users (username, password, role)
VALUES
('admin_user', 'adminpass', 'admin'),
('doctor_user', 'doctorpass', 'doctor'),
('client_user', 'clientpass', 'client');

CREATE TABLE Services (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

-- Insert sample services
INSERT INTO Services (service_name, description, price)
VALUES
('Consultation', 'General doctor consultation', 100.00),
('Massage', 'Relaxing full body massage', 150.00),
('Haircut', "Basic men's haircut", 50.00);

CREATE TABLE Availability (
    id SERIAL PRIMARY KEY,
    doctor_id INT REFERENCES Users(id),
    available_time TIMESTAMP NOT NULL
);

-- Insert sample availability for the doctor (assuming doctor_user has ID 2)
INSERT INTO Availability (doctor_id, available_time)
VALUES
(2, '2025-12-21 10:00:00'),
(2, '2025-12-21 14:00:00'),
(2, '2025-12-22 09:00:00');

CREATE TABLE Appointments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(id),
    service_id INT REFERENCES Services(id),
    appointment_time TIMESTAMP NOT NULL,
    status VARCHAR(50) CHECK (status IN ('pending', 'confirmed', 'completed', 'cancelled')) NOT NULL
);

-- Insert sample appointments
INSERT INTO Appointments (user_id, service_id, appointment_time, status)
VALUES
(3, 1, '2025-12-21 10:00:00', 'pending'),  -- client_user (id = 3) books a consultation
(3, 2, '2025-12-21 14:00:00', 'confirmed'); -- client_user (id = 3) books a massage

CREATE TABLE Payments (
    id SERIAL PRIMARY KEY,
    appointment_id INT REFERENCES Appointments(id),
    payment_date TIMESTAMP NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_status VARCHAR(50) CHECK (payment_status IN ('pending', 'paid', 'failed')) NOT NULL
);

-- Insert sample payments
INSERT INTO Payments (appointment_id, payment_date, amount, payment_status)
VALUES
(1, '2025-12-21 11:00:00', 100.00, 'paid'),  -- Payment for the first appointment
(2, '2025-12-21 15:00:00', 150.00, 'paid');  -- Payment for the second appointment
