import pefile
import sys
import os

file_path = "data-files\\virus-samples\\c6f30c532b2a5658ca0d8d6ab38b3484c0abfe519335298efeea62bf71a90056"
def analyze_pe_header(file_path):
    try:
        pe = pefile.PE(file_path)
    except Exception as e:
        print(f"Error: Cannot parse PE file ({e})")
        return

    print("[INFO] PE file detected.")
    
    print("Number of Sections:", pe.FILE_HEADER.NumberOfSections)
    print("TimeDateStamp:", pe.FILE_HEADER.TimeDateStamp)
    print("SizeOfOptionalHeader:", pe.FILE_HEADER.SizeOfOptionalHeader)
    print("Characteristics:", hex(pe.FILE_HEADER.Characteristics))
    print("SizeOfImage:", hex(pe.OPTIONAL_HEADER.SizeOfImage))
    print("AddressOfEntryPoint:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
    
    total_raw_size = sum(section.SizeOfRawData for section in pe.sections)
    if pe.OPTIONAL_HEADER.SizeOfImage > total_raw_size * 1.5:
        print("[ALERT] The SizeOfImage is significantly larger than the sum of section raw sizes. This may indicate that the file is packed or obfuscated.")
    else:
        print("[INFO] File header sizes appear consistent.")
    
    for section in pe.sections:
        try:
            entropy = section.get_entropy()
            section_name = section.Name.decode(errors="ignore").strip()
            print(f"Section {section_name} entropy: {entropy:.2f}")
            # High entropy (e.g. above 7.5) can be a flag for packing.
            if entropy > 7.5:
                print(f"[ALERT] Section '{section_name}' has high entropy, which might suggest it is packed.")
        except Exception as ex:
            print(f"Could not calculate entropy for section: {ex}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pe_analyzer.py <filename>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)
    
    analyze_pe_header(file_path)
