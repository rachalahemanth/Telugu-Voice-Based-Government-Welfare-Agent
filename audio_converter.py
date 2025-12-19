import os
import subprocess

def convert_aac_to_mp4_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Invalid folder path: {folder_path}")

    for file in os.listdir(folder_path):
        if file.lower().endswith(".aac"):
            input_path = os.path.join(folder_path, file)
            output_file = os.path.splitext(file)[0] + ".mp4"
            output_path = os.path.join(folder_path, output_file)

            command = [
                "ffmpeg",
                "-y",
                "-i", input_path,
                "-c", "copy",
                output_path
            ]

            subprocess.run(command, check=True)
            print(f"✅ Converted: {file} → {output_file}")

# ---------- RUN ----------
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(BASE_DIR, "audios")
    convert_aac_to_mp4_in_folder(folder)
