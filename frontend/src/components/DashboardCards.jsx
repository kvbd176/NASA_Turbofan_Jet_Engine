import { useEffect, useState } from "react";
import {
  FaHeartbeat,
  FaExclamationTriangle,
  FaClock,
  FaTools,
} from "react-icons/fa";

import API from "../services/api";

function DashboardCards() {

  const [kpis, setKpis] = useState({
    healthy: "--",
    critical: "--",
    average_rul: "--",
    maintenance: "--",
  });

  useEffect(() => {

    const fetchKPIs = async () => {
      try {

        const response = await API.get("/dashboard/kpis");

        console.log("KPIs:", response.data);

        setKpis({
          healthy: response.data.healthy_engines ?? "--",
          critical: response.data.critical_engines ?? "--",
          average_rul: response.data.average_rul ?? "--",
          maintenance: response.data.immediate_maintenance_engines ?? "--",
        });

      } catch (error) {
        console.error("Failed to fetch KPIs:", error);
      }
    };

    fetchKPIs();

  }, []);

  const cards = [
    {
      title: "Healthy Engines",
      value: kpis.healthy,
      icon: <FaHeartbeat className="text-purple-600 text-2xl" />,
    },
    {
      title: "Critical Engines",
      value: kpis.critical,
      icon: <FaExclamationTriangle className="text-purple-600 text-2xl" />,
    },
    {
      title: "Average RUL",
      value: kpis.average_rul,
      icon: <FaClock className="text-purple-600 text-2xl" />,
    },
    {
      title: "Maintenance",
      value: kpis.maintenance,
      icon: <FaTools className="text-purple-600 text-2xl" />,
    },
  ];

  return (
    <div className="grid grid-cols-2 gap-5">
      {cards.map((card, index) => (
        <div
          key={index}
          className="bg-white rounded-xl border border-gray-200 p-4 shadow-sm hover:shadow-md transition"
        >
          <div className="flex justify-between items-center">
            <div>
              <p className="text-gray-500 text-sm">
                {card.title}
              </p>

              <h2 className="text-2xl font-bold text-gray-800 mt-3">
                {card.value}
              </h2>
            </div>

            <div>{card.icon}</div>

          </div>
        </div>
      ))}
    </div>
  );
}

export default DashboardCards;