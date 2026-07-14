import Chat from "./components/Chat";
import Upload from "./components/Upload";

function App() {
    return (
        <div className="min-h-screen bg-gray-100">

            <header className="bg-blue-600 text-white p-4">
                <h1 className="text-xl font-bold">
                    Enterprise Knowledge Assistant
                </h1>
            </header>


            <div className="grid grid-cols-4 gap-4 p-6">

                <div className="col-span-1">
                    <Upload />
                </div>


                <div className="col-span-3">
                    <Chat />
                </div>

            </div>

        </div>
    );
}

export default App;