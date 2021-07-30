import express from "express";
import cors from "cors";
import http from "http";

const app = express();
app.use(express.json());
app.use(cors());

const PORT = process.env.PORT || 3001;

app.get("/", (req, res) => {
  return res.status(200).json({
    name: "node backend",
    programmer: "Gari",
    behind: "Express + MongoDB",
    language: "JavaScript",
  });
});

app.listen(PORT, () => console.log("The server has started!!"));
