import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Navbar() {

  const { user, logout } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

   const titles = {
    "/dashboard": "Dashboard",
    "/engine-status": "Engine Status",
    "/assistant": "AI Assistant",
    "/reports": "Reports",
    "/upload": "Upload Dataset"
  };

  const handleLogout = () => {

    if(window.confirm("Are you sure you want to logout?")){
      logout();
      navigate("/"); }
  };

  return (

    <div className="h-16 bg-white border-b flex items-center justify-between px-8">

      <h1 className="text-2xl font-bold text-purple-700">
        {titles[location.pathname] || "NASA AI"}
      </h1>

      <div className="flex items-center gap-4">

        <div className="text-right">

          <p className="text-sm text-gray-500">
            Logged in as
          </p>

          <p className="font-semibold text-gray-800">
            {user?.username || user?.email || "User"}
          </p>

        </div>

        <button
          onClick={handleLogout}
          className="bg-purple-700 hover:bg-purple-800 text-white px-4 py-2 rounded-lg"
        >
          Logout
        </button>

      </div>

    </div>

  );

}

export default Navbar;