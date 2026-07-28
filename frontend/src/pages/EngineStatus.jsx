import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import EngineTable from "../components/EngineTable";

function EngineStatus() {
  return (
    <div className="flex h-screen bg-gray-100">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Navbar />

        <div className="flex-1 p-6 overflow-hidden">
          <h1 className="text-3xl font-bold mb-6">
            Engine Status
          </h1>

          <EngineTable />
        </div>

      </div>

    </div>
  );
}

export default EngineStatus;