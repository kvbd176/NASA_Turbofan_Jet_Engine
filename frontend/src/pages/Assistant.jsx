import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import ChatBox from "../components/ChatBox";

function Assistant() {
  return (
    <div className="flex h-screen bg-gray-100">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Navbar />

        <div className="flex-1 p-6 overflow-hidden">
          <ChatBox />
        </div>

      </div>

    </div>
  );
}

export default Assistant;