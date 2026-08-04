import { useState, useEffect } from "react";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

import API from "../services/api";

function RiskChart() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  useEffect(() => {
    const load = async () => {
      try {
        const res = await API.get(
          "/analytics/risk-distribution"
        );
        console.log(
          "Risk Distribution:",
          JSON.stringify(res.data, null, 2)
        );
        if (Array.isArray(res.data)) {
          setData(
            res.data.map(item => ({
              name: item.risk_level,
              value: item.count,
            }))
          );
        } else {
          console.log(res.data.message);
          setData([]);
        }
      } catch (err) {
        console.error(
          "Failed to load risk distribution:",
          err
        );
        setError(true);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-5 shadow-sm">
      <h2 className="text-lg font-semibold text-gray-800 mb-4">
        Risk Distribution
      </h2>
      <div className="h-56 flex items-center justify-center">
        {
          loading ? (
            <div className="w-full h-full animate-pulse bg-gray-100 rounded-lg"></div>
          ) : error ? (
            <p className="text-gray-400">
              Unable to load risk data
            </p>
          ) : data.length === 0 ? (
            <p className="text-gray-400">
              No risk data available
            </p>
          ) : (
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar
                  dataKey="value"
                  fill="#7C3AED"
                  radius={[8, 8, 0, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          )
        }
      </div>
    </div>
  );
}

export default RiskChart;
