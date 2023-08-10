const express = require('express');
const mongoose = require('mongoose');
const Post = require('./models/post');

const app = express();
const PORT = 5000;

mongoose.connect('mongodb://localhost:27017/mydb', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.get('/api/posts', async (req, res) => {
  try {
   
    const postedDataSevenDaysAgo = new Date();
    postedDataSevenDaysAgo.setDate(postedDataSevenDaysAgo.getDate() - 7);
    const posts = await Post.find({ $or: [{ createdAt: { $gte: postedDataSevenDaysAgo } }, { updatedAt: { $gte: postedDataSevenDaysAgo } }] });

    res.json(posts);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});