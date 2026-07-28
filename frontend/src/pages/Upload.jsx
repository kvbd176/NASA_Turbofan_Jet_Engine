import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function Upload() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadDataset = async () => {
    if (!file) {
      setMessage("Please choose a dataset first.");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const res = await API.post(
        "/upload/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setMessage(res.data.message);
    } catch (err) {
      setMessage("Upload failed.");
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  const runPipeline = async () => {
    try {
      setLoading(true);

      const res = await API.post("/pipeline/run");

      setMessage("Pipeline completed successfully!");

      console.log(res.data);
    } catch (err) {
      console.log(err);
      setMessage("Pipeline failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 flex flex-col">

        {/* Navbar */}
        <Navbar />

        {/* Page Body */}
        <div className="flex-1 overflow-auto p-8">

          <div className="max-w-3xl mx-auto bg-white rounded-2xl shadow-lg p-10">

            <h1 className="text-4xl font-bold text-purple-700 mb-8">
              Upload Engine Dataset
            </h1>

            <label className="block text-lg font-semibold mb-3">
              Select Dataset
            </label>

            <input
              type="file"
              accept=".txt,.csv"
              onChange={(e) => setFile(e.target.files[0])}
              className="w-full border border-gray-300 rounded-lg p-3"
            />

            {file && (
              <p className="text-green-600 mt-4">
                Selected File: <b>{file.name}</b>
              </p>
            )}

            <div className="flex gap-4 mt-8">

              <button
                onClick={uploadDataset}
                disabled={loading}
                className="bg-purple-700 hover:bg-purple-800 text-white px-6 py-3 rounded-lg"
              >
                Upload Dataset
              </button>

              <button
                onClick={runPipeline}
                disabled={loading}
                className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg"
              >
                Run Pipeline
              </button>

            </div>

            {loading && (
              <div className="mt-6 text-blue-600 font-medium">
                Processing...
              </div>
            )}

            {message && (
              <div className="mt-6 bg-gray-100 border rounded-lg p-4">
                {message}
              </div>
            )}

          </div>

        </div>

      </div>

    </div>
  );
}

export default Upload;