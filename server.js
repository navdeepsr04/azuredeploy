require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const path = require("path");

const app = express();

// Middleware
app.use(express.json());
app.use(express.static("public"));

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI)
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

// Schema + Model
const UserSchema = new mongoose.Schema({
  naam: String,
  email: String
});

const User = mongoose.model("User", UserSchema);

// Routes

// Serve frontend
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Add user
app.post("/add-user", async (req, res) => {
    try {
      console.log("BODY:", req.body); 
  
      const { naam, email } = req.body;
  
      const newUser = new User({ naam, email });
      await newUser.save();
  
      res.json({ message: "User added successfully" });
    } catch (err) {
      console.log("ERROR:", err);
      res.status(500).json({ error: err.message });
    }
  });

// Get all users
app.get("/users", async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (err) {
    res.status(500).json({ error: "Error fetching users" });
  }
});

// Server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));