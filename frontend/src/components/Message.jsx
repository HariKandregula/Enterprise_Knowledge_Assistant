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

        </div>

    );
}