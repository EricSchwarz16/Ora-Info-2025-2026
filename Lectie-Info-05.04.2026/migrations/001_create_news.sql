CREATE TABLE IF NOT EXISTS news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    content TEXT,
    photo VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS views (
    id SERIAL PRIMARY KEY,
    date DATE DEFAULT CURRENT_DATE,
    news_id INTEGER REFERENCES news(id)
);
