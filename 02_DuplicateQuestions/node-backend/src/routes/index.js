import { Router } from "express";
import mongoose from "mongoose";
import uri from "../connection/index.js";
import History from "../models/index.js";
const router = Router();

mongoose
  .connect(uri, {
    useCreateIndex: true,
    useFindAndModify: true,
    useUnifiedTopology: true,
    useNewUrlParser: true,
  })
  .then(() => console.log("Connection has been established"))
  .catch((error) => console.log(error));

mongoose.connection.once("open", () => console.log("mongoose connection open"));

router.get("/", (req, res) => {
  return res.status(200).json({
    name: "node backend",
    programmer: "Gari",
    behind: "Express + MongoDB",
    language: "JavaScript",
  });
});

router.post("/history", async (req, res) => {
  const { date, question1, question2, classLabel, probability } = req.body;
  await History.create(
    {
      date,
      question1,
      question2,
      classLabel,
      probability,
    },
    (error, docs) => {
      if (error) {
        throw error;
      }
      return res.status(200).send(docs);
    }
  );
});

router.get("/histories", async (req, res) => {
  await History.find({}, (error, docs) => {
    if (error) {
      throw error;
    }
    return res.status(200).send(docs);
  });
});

export default router;
