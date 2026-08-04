import { useEffect, useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
} from "recharts";

import API from "../services/api";


const COLORS = [
  "#8b5cf6",
  "#c4b5fd",
  "#e5e7eb",
];


function HealthChart() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  useEffect(() => {
    async function load() {
      try {
        const res = await API.get(
          "/analytics/health-distribution"
        );
        const chartData = Object.entries(res.data)
          .map(([name, value]) => ({
            name,
            value,
          }));
        setData(chartData);
      } catch (err) {
        console.error(
          "Failed to load health distribution:",
          err
        );
        setError(true);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-5 shadow-sm">
      <h2 className="font-semibold text-gray-800 mb-4">
        Health Status
      </h2>
      <div className="h-56 flex items-center justify-center">
        {
          loading ? (
            <div className="w-full h-full animate-pulse bg-gray-100 rounded-lg"></div>
          ) : error ? (
            <p className="text-gray-400">
              Unable to load health data
            </p>
          ) : data.length === 0 ? (
            <p className="text-gray-400">
              No data available
            </p>
          ) : (
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={data}
                  dataKey="value"
                  nameKey="name"
                  innerRadius={55}
                  outerRadius={80}
                >
                  {
                    data.map((entry, index) => (
                      <Cell
                        key={index}
                        fill={COLORS[index % COLORS.length]}
                      />
                    ))
                  }
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          )
        }
      </div>
    </div>
  );
}

export default HealthChart;
