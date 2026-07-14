export default function Message({message}){

    return (

        <div
        className={`p-3 rounded mb-3 ${
            message.role==="user"
            ? "bg-blue-100 text-right"
            : "bg-gray-200"
        }`}
        >

            <p>
                {message.content}
            </p>


            {
                message.sources &&
                <div className="mt-2 text-sm text-gray-600">

                    <b>
                    Sources:
                    </b>

                    {
                        message.sources.map(
                            (src,index)=>(
                                <div key={index}>
                                    📄 {src}
                                </div>
                            )
                        )
                    }

                </div>
            }


        </div>

    );
}