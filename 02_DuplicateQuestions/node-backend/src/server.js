import express from "express";
import cors from "cors";
import router from "./routes/index.js";

const app = express();
app.use(express.json());
app.use(cors());
app.use(router);

const PORT = process.env.PORT || 3001;

app.listen(PORT, () => console.log("The server has started!!"));
