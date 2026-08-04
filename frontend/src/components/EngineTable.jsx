import { useEffect, useState } from "react";
import API from "../services/api";

function EngineTable() {
  const [engines, setEngines] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  useEffect(() => {
    const loadEngines = async () => {
      try {
        const res = await API.get(
          "/analytics/critical-engines"
        );
        console.log(
          "Critical Engines:",
          JSON.stringify(res.data, null, 2)
        );
        setEngines(Array.isArray(res.data) ? res.data : []
        );
      } catch (err) {
        console.error(
          "Failed to load critical engines:",
          err
        );
        setError(true);
      } finally {
        setLoading(false);
      }
    };
    loadEngines();
  }, []);

  return (
    <div className="w-full bg-white rounded-xl shadow-sm border border-gray-200 h-[79vh] flex flex-col">
      <div className="px-6 py-4 border-b">
        <h2 className="text-lg font-semibold">
          Critical Engines
        </h2>
      </div>
      <div className="flex-1 overflow-y-auto">
        <table className="w-full table-fixed">
          <thead className="sticky top-0 bg-white z-10 shadow-sm">
            <tr className="border-b">
              <th className="w-1/3 text-left px-6 py-3">
                Engine ID
              </th>
              <th className="w-1/3 text-left px-6 py-3">
                Predicted RUL
              </th>
              <th className="w-1/3 text-left px-6 py-3">
                Risk Level
              </th>
            </tr>
          </thead>
          <tbody>
            {
              loading ? (
                Array.from({ length: 6 }).map((_, index) => (
                  <tr
                    key={index}
                    className="border-b border-gray-200 animate-pulse"
                  >
                    <td className="px-6 py-4">
                      <div className="h-4 bg-gray-200 rounded w-20"></div>
                    </td>
                    <td className="px-6 py-4">
                      <div className="h-4 bg-gray-200 rounded w-16"></div>
                    </td>
                    <td className="px-6 py-4">
                      <div className="h-4 bg-gray-200 rounded w-24"></div>
                    </td>
                  </tr>
                ))
              ) : error ? (
                <tr>
                  <td
                    colSpan="3"
                    className="text-center py-10 text-gray-400"
                  >
                    Failed to load engine data
                  </td>
                </tr>
              ) : engines.length === 0 ? (
                <tr>
                  <td
                    colSpan="3"
                    className="text-center py-10 text-gray-400"
                  >
                    No critical engines found
                  </td>
                </tr>
              ) : (
                engines.map((engine, index) => (
                  <tr
                    key={index}
                    className="border-b border-gray-200 hover:bg-purple-50 transition"
                  >
                    <td className="px-6 py-3">
                      {engine.engine_id}
                    </td>
                    <td className="px-6 py-3">
                      {engine.Predicted_RUL}
                    </td>
                    <td className="px-6 py-3">
                      {engine.Risk_Level}
                    </td>
                  </tr>
                ))
              )
            }
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default EngineTable;
