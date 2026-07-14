import { useState } from "react";
import { uploadDocument } from "../api/client";


export default function Upload(){

    const [file,setFile] = useState(null);
    const [message,setMessage] = useState("");

    const handleUpload = async()=>{

        if(!file)
            return;


        try{

            await uploadDocument(file);

            setMessage(
                "Document uploaded successfully"
            );

        }
        catch(error){

            setMessage(
                "Upload failed"
            );
        }

    };


    return (

        <div className="bg-white p-5 rounded shadow">

            <h2 className="font-bold mb-3">
                Upload Knowledge
            </h2>


            <input
                type="file"
                onChange={(e)=>
                    setFile(e.target.files[0])
                }
            />


            <button
                onClick={handleUpload}
                className="bg-blue-600 text-white px-4 py-2 mt-4 rounded"
            >
                Upload
            </button>


            <p className="mt-3 text-sm">
                {message}
            </p>

        </div>

    );
}