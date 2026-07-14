import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000/api",
});

export const askQuestion = (question) =>
    API.post("/chat/", {
        question,
    });

export const uploadDocument = (file) => {
    const formData = new FormData();
    formData.append("file", file);

    return API.post("/documents/upload/", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });
};