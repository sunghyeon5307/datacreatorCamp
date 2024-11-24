from google.colab import drive
drive.mount('/content/drive') 

!unzip -qq '/content/drive/MyDrive/데이터 분석 대회/training.zip' -d 'training' 
!unzip -qq '/content/drive/MyDrive/데이터 분석 대회/test.zip' -d 'test' 