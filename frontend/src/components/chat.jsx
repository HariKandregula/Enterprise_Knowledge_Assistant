import {useState} from "react";
import Message from "./Message";
import {askQuestion} from "../api/client";


export default function Chat(){


    const [messages,setMessages]=useState([]);

    const [question,setQuestion]=useState("");

    const [loading,setLoading]=useState(false);



    const sendMessage = async()=>{


        if(!question)
            return;


        const userMessage={
            role:"user",
            content:question
        };


        setMessages(prev=>[
            ...prev,
            userMessage
        ]);


        setQuestion("");
        setLoading(true);



        try{

            const response =
                await askQuestion(
                    question
                );


            const aiMessage={

                role:"assistant",

                content:
                response.data.answer,


                sources:
                response.data.sources

            };


            setMessages(prev=>[
                ...prev,
                aiMessage
            ]);

        }
        catch(error){

            setMessages(prev=>[
                ...prev,
                {
                    role:"assistant",
                    content:
                    "Something went wrong"
                }
            ]);

        }


        setLoading(false);

    };



    return (

        <div className="bg-white rounded shadow p-5">


            <div className="h-[500px] overflow-y-auto mb-4">

                {
                    messages.map(
                        (msg,index)=>(
                            <Message
                            key={index}
                            message={msg}
                            />
                        )
                    )
                }


                {
                    loading &&
                    <p>
                    AI is thinking...
                    </p>
                }


            </div>



            <div className="flex gap-2">


                <input

                value={question}

                onChange={(e)=>
                    setQuestion(e.target.value)
                }

                placeholder="Ask about company documents..."

                className="border flex-1 p-2 rounded"

                />


                <button

                onClick={sendMessage}

                className="bg-blue-600 text-white px-5 rounded"

                >
                    Send
                </button>


            </div>


        </div>

    );
}