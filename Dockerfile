FROM python:3
RUN git clone https://github.com/FranciscoLopezGarcia/Proyecto_4_En_Linea.git
WORKDIR /4-in-line-FranciscoLopezGarcia
RUN pip install -r requirements.txt
CMD ["python3",  "-m", "unittest"]
