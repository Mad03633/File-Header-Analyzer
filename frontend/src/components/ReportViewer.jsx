import React from "react";

export default function ReportViewer({ report }) {
  if (!report) return null;

  return (
    <div className="bg-white p-6 rounded-xl shadow border border-gray-200 mt-6">
      <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">
        Analysis Report
      </h2>

      <table className="w-full table-fixed text-sm text-left text-gray-800 border border-collapse">
        <thead className="bg-gray-100">
          <tr>
            <th className="w-1/4 p-2 border font-semibold">Section</th>
            <th className="w-1/4 p-2 border font-semibold">Field</th>
            <th className="w-1/2 p-2 border font-semibold">Value</th>
          </tr>
        </thead>
        <tbody>
          {/* General Info */}
          <tr className="border-t-2 border-gray-300">
            <td className="p-2 font-bold text-blue-700 border">General Info</td>
            <td className="p-2 border">File ID</td>
            <td className="p-2 border">{report.id}</td>
          </tr>
          <tr>
            <td></td>
            <td className="p-2 border">Filename</td>
            <td className="p-2 border">{report.filename}</td>
          </tr>

          {/* Signature */}
          {report.signature && (
            <>
              <tr className="border-t-2 border-gray-300">
                <td className="p-2 font-bold text-blue-700 border">Signature</td>
                <td className="p-2 border">Match</td>
                <td className="p-2 border">{report.signature.match ? "✅ Yes" : "❌ No"}</td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Extension</td>
                <td className="p-2 border">{report.signature.extension}</td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Header Signature</td>
                <td className="p-2 border">{report.signature.signature}</td>
              </tr>
                  <tr>
                    <td></td>
                    <td className="p-2 border">MIME Type</td>
                    <td className="p-2 border">{report.signature.mime_type || "Not defined"}</td>
                  </tr>
            </>
          )}

          {/* Entropy */}
          {report.entropy && (
            <>
              <tr className="border-t-2 border-gray-300">
                <td className="p-2 font-bold text-blue-700 border">Entropy</td>
                <td className="p-2 border">Value</td>
                <td className="p-2 border">{report.entropy.entropy}</td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Risk</td>
                <td
                  className={`p-2 border ${
                    report.entropy.risk === "High" ? "text-red-600 font-semibold" : ""
                  }`}
                >
                  {report.entropy.risk}
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Entropy Category</td>
                <td className="p-2 border">{report.entropy.entropy_category}</td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Most Frequent Byte</td>
                <td className="p-2 border">
                  <code>{report.entropy.top_byte}</code>
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Data Length (bytes)</td>
                <td className="p-2 border">{report.entropy.length_bytes}</td>
              </tr>
              {report.entropy.note && (
                <tr>
                  <td></td>
                  <td className="p-2 border">Note</td>
                  <td className="p-2 border italic text-gray-600">{report.entropy.note}</td>
                </tr>
              )}
            </>
          )}

          {/* Validation */}
          {report.validation && (
            <>
              <tr className="border-t-2 border-gray-300">
                <td className="p-2 font-bold text-blue-700 border">Validation</td>
                <td className="p-2 border">Format Type</td>
                <td className="p-2 border">{report.validation.type}</td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Valid</td>
                <td className="p-2 border">
                  {report.validation.valid ? "✅ Yes" : "❌ No"}
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Header Bytes</td>
                <td className="p-2 border">
                  <code>{report.validation.header_bytes}</code>
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Expected Signature</td>
                <td className="p-2 border">
                  <code>{report.validation.expected_signature}</code>
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Validation Method</td>
                <td className="p-2 border">{report.validation.method}</td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Bytes Read</td>
                <td className="p-2 border">{report.validation.bytes_read}</td>
              </tr>
              {report.validation.note && (
                <tr>
                  <td></td>
                  <td className="p-2 border">Note</td>
                  <td className="p-2 border text-yellow-700 italic">{report.validation.note}</td>
                </tr>
              )}
            </>
          )}

          {/* C++ Analysis */}
          {report.cpp_analysis && (
            <>
              <tr className="border-t-2 border-gray-300">
                <td className="p-2 font-bold text-blue-700 border">C++ Analysis</td>
                <td className="p-2 border">Header Preview</td>
                <td className="p-2 border">
                  <code>{report.cpp_analysis.header_preview}</code>
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Heuristic</td>
                <td className="p-2 border">{report.cpp_analysis.heuristic}</td>
              </tr>
              {report.cpp_analysis.file_size && (
                <tr>
                  <td></td>
                  <td className="p-2 border">File Size (bytes)</td>
                  <td className="p-2 border">{report.cpp_analysis.file_size}</td>
                </tr>
              )}
            </>
          )}

          {/* VirusTotal Link */}
          {report.virustotal && (
            <>
              <tr className="border-t-2 border-gray-300">
                <td className="p-2 font-bold text-blue-700 border">VirusTotal</td>
                <td className="p-2 border">Permalink</td>
                <td className="p-2 border">
                  <a
                    href={report.virustotal.permalink}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-600 underline"
                  >
                    Open VirusTotal Report ↗
                  </a>
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Scan ID</td>
                <td className="p-2 border">{report.virustotal.id}</td>
              </tr>
            </>
          )}

          {/* Verdict */}
          {report.verdict && (
            <>
              <tr className="border-t-2 border-gray-300">
                <td className="p-2 font-bold text-blue-700 border">Verdict</td>
                <td className="p-2 border">Status</td>
                <td
                  className={`p-2 border font-semibold ${
                    report.verdict.status.includes("❗") ? "text-red-600" : "text-green-600"
                  }`}
                >
                  {report.verdict.status}
                </td>
              </tr>
              <tr>
                <td></td>
                <td className="p-2 border">Risk</td>
                <td className="p-2 border">{report.verdict.risk}</td>
              </tr>
            </>
          )}
        </tbody>
      </table>
    </div>
  );
}
