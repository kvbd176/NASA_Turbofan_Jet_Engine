import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { Mail, Lock, Eye, EyeOff } from "lucide-react";
import AuthHero from "../components/AuthHero";

function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!email || !password) {
      setError("Please fill in all required fields.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      await login(email, password);

      navigate("/dashboard");
    } catch (err) {
      setError(err.response?.data?.detail || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex bg-gray-100">

      <AuthHero />

        <div className="flex w-full lg:w-1/2 items-center justify-center p-8">

        <div className="bg-white shadow-2xl rounded-2xl p-10 w-full max-w-md">

        <div className="text-center mb-8">

          <h1 className="text-3xl font-bold text-purple-700">
            NASA Turbofan
          </h1>

          <p className="text-gray-600 mt-2">
            Predictive Maintenance System
          </p>

          <p className="text-sm text-gray-500 mt-1">
            Sign in to continue
          </p>

        </div>

        {error && (
          <div className="mb-5 rounded-lg bg-red-100 border border-red-300 text-red-700 p-3 text-sm">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>

          <label className="block mb-2 text-sm font-medium text-gray-700">
            Email Address <span className="text-red-500">*</span>
          </label>

          <div className="relative mb-5">

            <Mail
              size={18}
              className="absolute left-3 top-3.5 text-gray-400"
            />

            <input
              type="email"
              placeholder="Enter your email"
              className="w-full pl-10 pr-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

          </div>

          <label className="block mb-2 text-sm font-medium text-gray-700">
            Password <span className="text-red-500">*</span>
          </label>

          <div className="relative mb-3">

            <Lock
              size={18}
              className="absolute left-3 top-3.5 text-gray-400"
            />

            <input
              type={showPassword ? "text" : "password"}
              placeholder="Enter your password"
              className="w-full pl-10 pr-12 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <button
              type="button"
              className="absolute right-3 top-3 text-gray-500"
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? <Eye size={20} /> : <EyeOff size={20} />}
            </button>

          </div>

          <div className="flex justify-between items-center mb-6">

            <label className="flex items-center gap-2 text-sm text-gray-600">

              <input type="checkbox" />

              Remember Me

            </label>

            <button
              type="button"
              className="text-sm text-purple-700 hover:underline"
            >
              Forgot Password?
            </button>

          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-purple-700 hover:bg-purple-800 text-white font-semibold py-3 rounded-lg transition duration-300"
          >
            {loading ? "Signing In..." : "Login"}
          </button>

        </form>

        <p className="text-center text-sm text-gray-600 mt-6">

          Don't have an account?{" "}

          <Link
            to="/register"
            className="text-purple-700 font-semibold hover:underline"
          >
            Register
          </Link>

        </p>

      </div>
      </div>
    </div>
  );
}

export default Login;