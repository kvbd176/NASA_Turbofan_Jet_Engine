import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import API from "../services/api";

function Reports() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  useEffect(() => {
    loadReport();
  }, []);

  const loadReport = async () => {
    try {
      const res = await API.get("/reports/system");
      setReport(res.data);
    } catch (err) {
      console.error(
        "Failed to load report:",
        err
      );
      setError(true);
    } finally {
      setLoading(false);
    }
  };
  const cards = [
    {
      title: "Total Engines",
      value: report?.Total_Engines,
    },
    {
      title: "Healthy",
      value: report?.Healthy_Engines,
    },
    {
      title: "Critical",
      value: report?.Critical_Engines,
    },
    {
      title: "Average RUL",
      value: report?.Average_RUL,
    },
    {
      title: "High Risk",
      value: report?.High_Risk_Engines,
    },
    {
      title: "Immediate Maintenance",
      value: report?.Immediate_Maintenance_Engines,
    },
  ];

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <div className="p-8 overflow-auto">
          <h1 className="text-3xl font-bold text-purple-700 mb-8">
            System Report
          </h1>
          {
            loading ? (
              <div className="grid grid-cols-2 gap-6">
                {
                  Array.from({length:6}).map((_,index)=>(
                    <div
                      key={index}
                      className="bg-white rounded-xl border border-gray-200 p-6 animate-pulse"
                    >
                      <div className="h-4 bg-gray-200 rounded w-28"></div>
                      <div className="h-10 bg-gray-200 rounded w-20 mt-4"></div>
                    </div>
                  ))
                }
              </div>
            ) : error ? (
              <div className="bg-white rounded-xl border p-8 text-gray-500">
                Failed to load system report.
              </div>
            ) : !report ? (
              <div className="bg-white rounded-xl border p-8 text-gray-500">
                No report data available.
              </div>
            ) : (
              <div className="grid grid-cols-2 gap-6">
                {
                  cards.map((card,index)=>(
                    <div
                      key={index}
                      className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition"
                    >
                      <h3 className="text-gray-500 text-sm font-medium">
                        {card.title}
                      </h3>
                      <p className="mt-2 text-3xl font-bold text-purple-700">
                        {card.value ?? "--"}
                      </p>
                    </div>
                  ))
                }
              </div>
            )
          }
        </div>
      </div>
    </div>
  );
}

export default Reports;
