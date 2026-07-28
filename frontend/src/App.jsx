import { Routes, Route, Navigate } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ProtectedRoute from "./components/ProtectedRoute";
import EngineStatus from "./pages/EngineStatus";
import Assistant from "./pages/Assistant";
import Reports from "./pages/Reports";
import Upload from "./pages/Upload";
import Pipeline from "./pages/Pipeline";

function App() {
  return (
    <Routes>

      <Route
        path="/"
        element={<Navigate to="/login" replace />}
      />

      <Route
        path="/login"
        element={<Login />}
      />

      <Route
        path="/register"
        element={<Register />}
      />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/upload"
        element={
          <ProtectedRoute>
            <Upload />
          </ProtectedRoute>
        }
      />

      <Route
        path="/engine-status"
        element={
            <ProtectedRoute>
                <EngineStatus />
            </ProtectedRoute>
        }
      />

      <Route
        path="/assistant"
        element={
            <ProtectedRoute>
                <Assistant />
            </ProtectedRoute>
        }
      />

      <Route
        path="/reports"
        element={
            <ProtectedRoute>
                <Reports />
            </ProtectedRoute>
        }
      />

      <Route
        path="/upload"
        element={
          <ProtectedRoute>
            <Upload />
          </ProtectedRoute>
        }
      />

      <Route
        path="/pipeline"
        element={
          <ProtectedRoute>
            <Pipeline />
          </ProtectedRoute>
        }
      />

    </Routes>
  );
}

export default App;