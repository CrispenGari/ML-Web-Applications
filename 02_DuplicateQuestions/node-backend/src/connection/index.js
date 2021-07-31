import dotenv from "dotenv";
dotenv.config();
console.log(process.env.PASSWORD);
const connection = `mongodb+srv://crispen:backend_history@cluster0.dxb60.mongodb.net/history?retryWrites=true&w=majority`;
export default connection;
