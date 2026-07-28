import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import DashboardCards from "../components/DashboardCards";
import HealthChart from "../components/HealthChart";
import RiskChart from "../components/RiskChart";
import EngineTable from "../components/EngineTable";
import ChatBox from "../components/ChatBox";

function Dashboard() {
  return (
    <div className="flex h-screen bg-gray-100 overflow-hidden">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">

        {/* Top Navbar */}
        <Navbar />

        {/* Dashboard Body */}
        <div className="flex flex-1 overflow-hidden">

          {/* Left Section */}
          <main className="flex-1 overflow-y-auto p-6 bg-gray-100">

            <DashboardCards />

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6 my-6">
              <HealthChart />
              <RiskChart />
            </div>

            <EngineTable />

          </main>

          {/* Right Chat Section */}
          <aside className="w-[360px] border-l bg-white">
            <ChatBox />
          </aside>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;