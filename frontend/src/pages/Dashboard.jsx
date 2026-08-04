import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import DashboardCards from "../components/DashboardCards";
import HealthChart from "../components/HealthChart";
import RiskChart from "../components/RiskChart";
import EngineTable from "../components/EngineTable";
import ChatBox from "../components/ChatBox";
import FullPageLoader from "../components/FullPageLoader";


function Dashboard() {
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false);
    }, 800);
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return <FullPageLoader />;
  }

  return (
    <div className="flex h-screen bg-gray-100 overflow-hidden">
      <Sidebar />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Navbar />
        <div className="flex flex-1 overflow-hidden">
          <main className="flex-1 overflow-y-auto p-6 bg-gray-100">
            <DashboardCards />
            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6 my-6">
              <HealthChart />
              <RiskChart />
            </div>
            <EngineTable />
          </main>
          <aside className="w-[360px] border-l bg-white">
            <ChatBox />
          </aside>
        </div>
      </div>
    </div>
  );
}
export default Dashboard;
