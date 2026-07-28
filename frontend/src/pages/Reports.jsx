import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import API from "../services/api";

function Reports() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    loadReport();
  }, []);

  const loadReport = async () => {
    try {
      const res = await API.get("/reports/system");
      setReport(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Navbar />

        <div className="p-8 overflow-auto">

          <h1 className="text-3xl font-bold text-purple-700 mb-8">
            System Report
          </h1>

          {!report ? (

            <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-8">
              Loading...
            </div>

          ) : (

            <div className="grid grid-cols-2 gap-6">

            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
              <h3 className="text-gray-500 text-sm font-medium">
                Total Engines
              </h3>
              <p className="mt-2 text-3xl font-bold text-purple-700">
                {report.Total_Engines}
              </p>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
              <h3 className="text-gray-500 text-sm font-medium">
                Healthy
              </h3>
              <p className="mt-2 text-3xl font-bold text-purple-700">
                {report.Healthy_Engines}
              </p>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
              <h3 className="text-gray-500 text-sm font-medium">
                Critical
              </h3>
              <p className="mt-2 text-3xl font-bold text-purple-700">
                {report.Critical_Engines}
              </p>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
              <h3 className="text-gray-500 text-sm font-medium">
                Average RUL
              </h3>
              <p className="mt-2 text-3xl font-bold text-purple-700">
                {report.Average_RUL}
              </p>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
              <h3 className="text-gray-500 text-sm font-medium">
                High Risk
              </h3>
              <p className="mt-2 text-3xl font-bold text-purple-700">
                {report.High_Risk_Engines}
              </p>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition">
              <h3 className="text-gray-500 text-sm font-medium">
                Immediate Maintenance
              </h3>
              <p className="mt-2 text-3xl font-bold text-purple-700">
                {report.Immediate_Maintenance_Engines}
              </p>
            </div>

          </div>

          )}

        </div>

      </div>

    </div>
  );
}

export default Reports;