import os
import subprocess

def compress_videos_in_folder(folder_path):
    # Assicurati che la cartella esista
    if not os.path.isdir(folder_path):
        print(f"Il percorso {folder_path} non è una cartella valida.")
        return

    # Loop attraverso tutti i file nella cartella
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Controlla se il file è un video (controllo semplice tramite estensione)
        if filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')):
            output_file = os.path.join(folder_path, f"compressed_{filename}")

            # Comando ffmpeg per comprimere il video
            command = [
                'ffmpeg',
                '-i', file_path,             # Input file
                '-vcodec', 'libx265',        # Codec video (H.265)
                '-crf', '28',                # Constant Rate Factor (qualità, più alto = più compressione)
                '-preset', 'slow',           # Imposta un preset più lento per una migliore compressione
                '-c:a', 'aac',               # Codec audio (AAC)
                '-b:a', '128k',              # Bitrate audio
                output_file                  # Output file
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Video compresso: {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Errore durante la compressione di {file_path}: {e}")

if __name__ == "__main__":
    folder_path = "C:/Users/d.lalla/Desktop/videos"  # Sostituisci con il percorso della tua cartella
    compress_videos_in_folder(folder_path)
