import dotenv from "dotenv";
dotenv.config();
import password from "../constants/keys.js";
const connection = `mongodb+srv://crispen:${password}@cluster0.dxb60.mongodb.net/history?retryWrites=true&w=majority`;
export default connection;
