import struct

def validate_format(file_path):
    try:
        with open(str(file_path), 'rb') as f:
            data = f.read(12)
    except Exception as e:
        return {"error": str(e)}

    magic_hex = " ".join(f"{b:02X}" for b in data)
    length = len(data)

    def result(format_type, expected_sig, method="startsWith", note=""):
        return {
            "type": format_type,
            "valid": True,
            "header_bytes": magic_hex,
            "expected_signature": expected_sig,
            "method": method,
            "bytes_read": length,
            "note": note
        }

    if data.startswith(b'MZ'):
        return result("PE", "4D 5A")
    if data.startswith(b'%PDF'):
        return result("PDF", "25 50 44 46")
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return result("PNG", "89 50 4E 47 0D 0A 1A 0A")
    if data.startswith(b'\xFF\xD8\xFF'):
        return result("JPG", "FF D8 FF")
    if data.startswith(b'PK\x03\x04'):
        return result("ZIP", "50 4B 03 04")
    if data.startswith(b'Rar!\x1A\x07'):
        return result("RAR", "52 61 72 21 1A 07")
    if data.startswith(b'GIF87a'):
        return result("GIF", "47 49 46 38 37 61", method="exact")
    if data.startswith(b'GIF89a'):
        return result("GIF", "47 49 46 38 39 61", method="exact")
    if data.startswith(b'7z\xBC\xAF\x27\x1C'):
        return result("7Z", "37 7A BC AF 27 1C")
    if data.startswith(b'\x7FELF'):
        return result("ELF", "7F 45 4C 46")
    if data.startswith(b'\xD0\xCF\x11\xE0'):
        return result("OLE", "D0 CF 11 E0")
    if data.startswith(b'ID3'):
        return result("MP3", "49 44 33")
    if data.startswith(b'\x00\x00\x00\x18ftypmp42'):
        return result("MP4", "00 00 00 18 66 74 79 70 6D 70 34 32")

    return {
        "type": "Unknown",
        "valid": False,
        "header_bytes": magic_hex,
        "expected_signature": "N/A",
        "method": "none",
        "bytes_read": length,
        "note": "No matching signature found"
    }
