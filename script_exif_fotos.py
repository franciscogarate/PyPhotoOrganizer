# Make: Marca de la cámara (ej. "Canon", "Nikon").
# Model: Modelo de la cámara (ej. "EOS 5D Mark IV", "D850").
# LensMake: Marca del objetivo/lente utilizado.
# LensModel: Modelo del objetivo/lente utilizado.
# ExposureTime: Tiempo de exposición o velocidad de obturación (ej. "1/200", "0.005s").
# FNumber: Valor de apertura (ej. "f/2.8").
# ISO: Sensibilidad ISO (ej. "100", "400").
# FocalLength: Longitud focal en milímetros (ej. "50mm").
# FocalLengthIn35mmFilm: Longitud focal equivalente en un sensor de 35mm (ej. "75mm").
# Flash: Información sobre si el flash se usó o no y en qué modo.
# WhiteBalance: Balance de blancos utilizado (ej. "Auto", "Manual").
# MeteringMode: Modo de medición de la exposición (ej. "Pattern", "CenterWeighted").
# ExposureProgram: Programa de exposición (ej. "Manual", "Aperture priority").
# ExposureBiasValue: Compensación de la exposición (ej. "+1 EV", "-0.5 EV").
# MaxApertureValue: Máxima apertura del objetivo en uso.
# DateTimeOriginal: Fecha y hora en que se tomó la foto.
# DateTimeDigitized: Fecha y hora en que se digitalizó la imagen (generalmente la misma que DateTimeOriginal).
# DateTime: Fecha y hora en que se guardó la imagen en el archivo.
# GPSLatitude: Latitud donde se tomó la foto.
# GPSLongitude: Longitud donde se tomó la foto.
# FileSource: Fuente del archivo (ej. "Digital Camera").
import subprocess
import pandas as pd

df = pd.read_excel('info_exif.xlsx')
df['Lon'] = df['Lon'].fillna(0).round(5)
df['Lat'] = df['Lat'].fillna(0).round(5)
df['DateTimeOriginal'] = pd.to_datetime(df['DateTimeOriginal'], dayfirst=True)
df['DateTimeOriginal'] = df['DateTimeOriginal'].dt.strftime('%Y:%m:%d %H:%M:%S')


for i in df.index:
    file_path = df['File'][i]
    make = df['Make'][i]
    model = df['Model'][i]
    lensmodel = df['LensModel'][i]
    focal = df['Focal'][i]
    iso = df['ISO'][i].astype(int)
    dia = df['DateTimeOriginal'][i]
    lat = df['Lat'][i]
    lon = df['Lon'][i]
    # Comando para cambiar los metadatos
    command = ["exiftool",
                f"-Make={make}",
                f"-Model={model}",
                f"-LensModel={lensmodel}",
                f"-FocalLength={focal}",
                f"-ISO={iso}",
                f"-DateTimeOriginal='{dia}'",
                f"-GPSLatitude={lat}",
                "-GPSLatitudeRef=N",
                f"-GPSLongitude={lon}",
                "-GPSLongitudeRef=W",
                "-Artist=Paco",
                "-By-line=Paco",
                "-Creator=Paco",
                "-overwrite_original",
                f"{file_path}"
            ]
    # Ejecutar el comando
    subprocess.run(command)
    #print(command)