import axios from 'axios';
//create an axios instance with a base URL
const api : AxiosInstance = axios.create({
    baseURL: 'http://localhost:8000',// Replace with your FastAPI backend URL
});
//Export the api instance for use in other parts of the application
export default api;