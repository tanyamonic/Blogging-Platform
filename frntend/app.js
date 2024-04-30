// app.js

const express = require('express');
const { Sequelize, DataTypes } = require('sequelize');

// Initialize Express app
const app = express();
const port = 3000;

// Database setup
const sequelize = new Sequelize('blog_db', 'blog_user', 'password', {
  dialect: 'postgres',
  host: 'localhost',
});

// Define models
const Post = sequelize.define('Post', {
  title: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  content: {
    type: DataTypes.TEXT,
    allowNull: false,
  },
});

// Sync models with the database
sequelize.sync().then(() => {
  console.log('Database & tables created!');
}).catch(err => {
  console.error('Error syncing database:', err);
});

// Routes
app.get('/posts', async (req, res) => {
  try {
    const posts = await Post.findAll();
    res.json(posts);
  } catch (error) {
    console.error('Error fetching posts:', error);
    res.status(500).json({ error: 'Error fetching posts' });
  }
});

// Add more routes as needed

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
