#para esse projeto é necessário a instalação da biblioteca pytube

from pytube import YouTube

url=input("Digite a url do youtube: \n")
formato=input("informe o formato, somente audio ou video: \n")
caminho=input("informe o local que deseja salvar: \n")


video = YouTube(url)
if formato == "video":
  video.streams.get_highest_resolution().download(
    output_path =f"{caminho}"
  )
elif formato == "audio":
  video.streams.filter(only_audio=True).first().download(
    output_path =f"{caminho}",
    filename=video.title + ".mp3"
  )
