import mongoose from "mongoose";

const History = new mongoose.Schema({
  date: {
    type: String,
    required: true,
  },
  question1: {
    type: String,
    required: true,
  },
  question2: {
    type: String,
    required: true,
  },
  classLabel: {
    type: String,
    required: true,
  },
  probability: {
    type: Number,
    required: true,
  },
});

const model = mongoose.models.Histories
  ? mongoose.models.Histories
  : mongoose.model("Histories", History);

export default model;
