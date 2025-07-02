import React, { useState } from "react";
import axios from "axios";

export default function FileUploader({ setReport }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://IP:PORT/upload", formData);
      setReport(res.data);
    } catch (err) {
      alert("Failed to analyze file.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-4 items-center justify-center"
    >
      <label className="relative cursor-pointer rounded-full bg-blue-600 text-white font-semibold px-6 py-2 hover:bg-blue-700 transition">
        Choose File
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
        />
      </label>

      {file && (
        <p className="text-sm text-gray-600">Selected: {file.name}</p>
      )}

      <button
        type="submit"
        disabled={loading}
        className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-bold py-2 px-6 rounded-lg shadow-md hover:shadow-lg transition disabled:opacity-50"
      >
        {loading ? "Analyzing..." : "Upload and Analyze"}
      </button>
    </form>
  );
}
