import React, { useState } from "react";
import FileUploader from "./components/FileUploader";
import ReportViewer from "./components/ReportViewer";

export default function App() {
  const [report, setReport] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 px-4 py-10 space-y-8">
      <div className="w-full max-w-3xl mx-auto bg-white p-6 rounded-2xl shadow-md">
        <h1 className="text-2xl font-bold text-center text-gray-800 mb-4">
          File Header Analyzer
        </h1>
        <FileUploader setReport={setReport} />
      </div>

      {report && (
        <div className="w-full max-w-6xl mx-auto">
          <ReportViewer report={report} />
        </div>
      )}
    </div>
  );
}
