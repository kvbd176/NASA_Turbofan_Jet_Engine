import { FaHome, FaChartBar, FaRobot, FaFileAlt } from "react-icons/fa";

import { NavLink } from "react-router-dom";
import { FaUpload } from "react-icons/fa";

function Sidebar() {

  const menus = [
    {
      icon: <FaHome />,
      text: "Dashboard",
      path: "/dashboard",
    },
    {
      icon: <FaUpload />,
      text: "Upload Dataset",
      path: "/upload",
    },
    {
      icon: <FaChartBar />,
      text: "Engine Status",
      path: "/engine-status",
    },
    {
      icon: <FaRobot />,
      text: "AI Assistant",
      path: "/assistant",
    },
    {
      icon: <FaFileAlt />,
      text: "Reports",
      path: "/reports",
    },
  ];

  return (
    <div className="w-60 bg-white border-r h-screen flex flex-col">

      <div className="p-6 border-b">
        <h1 className="text-3xl font-bold text-purple-700">
            NASA AI
        </h1>

        <p className="text-gray-500 text-sm">
            Predictive Maintenance
        </p>
    </div>

      <div className="mt-4">

        {menus.map((menu) => (

          <NavLink
            key={menu.text}
            to={menu.path}
            className={({ isActive }) =>
              `mx-3 mb-2 rounded-lg px-4 py-3 flex items-center gap-3 transition-all duration-200 ${
                isActive
                  ? "bg-purple-100 text-purple-700 font-semibold"
                  : "text-gray-700 hover:bg-gray-100"
              }`
            }
          >
            {menu.icon}
            {menu.text}
          </NavLink>

        ))}

      </div>

    </div>
  );
}

export default Sidebar;