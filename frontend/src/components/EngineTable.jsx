import { useEffect, useState } from "react";
import API from "../services/api";

function EngineTable() {

  const [engines, setEngines] = useState([]);

  useEffect(() => {

    const loadEngines = async () => {

      try {

        const res = await API.get("/analytics/critical-engines");

        console.log("Critical Engines:", JSON.stringify(res.data, null, 2));

        setEngines(Array.isArray(res.data) ? res.data : []);

      } catch (err) {

        console.log(err);

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

            {engines.map((engine, index) => (
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
            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default EngineTable;